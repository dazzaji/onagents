import json
import os
from typing import Dict, List, Optional, Union

from dotenv import load_dotenv
import anthropic
import google.generativeai as genai
from google.api_core import retry
from google.api_core import exceptions as google_exceptions
import logging
from tqdm import tqdm

# Set up logging
logging.basicConfig(level=logging.DEBUG, filename='script.log', filemode='w')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Anthropic and Gemini API clients
anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configuration for LLM interactions
MAX_ITERATIONS = 3  # Maximum number of revision loops
CLAUDE_MODEL = "claude-3-5-sonnet-20240620"  # Specific Claude model
GEMINI_MODEL = "gemini-1.5-pro"  # Specific Gemini model


def load_revised_plan(filename: str) -> Optional[Dict]:
    """Loads the revised project plan from JSON."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error loading revised project plan: {e}")
        return None


def get_claude_response(prompt: str) -> Optional[str]:
    """Gets a response from Claude using the Messages API."""
    try:
        response = anthropic_client.messages.create(
            model=CLAUDE_MODEL,
            messages=[{"role": "user", "content": prompt}],  # Messages API format
            max_tokens=2048,  # Use max_tokens instead of max_tokens_to_sample
            temperature=0,
        )
        return response.content[0].text  # Extract the text from the response
    except Exception as e:
        logger.error(f"Error getting response from Claude: {e}")
        return None


def get_gemini_response(prompt: str) -> Optional[str]:
    """Gets a response from Gemini with error handling and retry logic."""
    model = genai.GenerativeModel(GEMINI_MODEL)

    @retry.Retry(predicate=retry.if_exception_type(
        google_exceptions.ResourceExhausted,
        google_exceptions.ServiceUnavailable,
        google_exceptions.DeadlineExceeded,
        google_exceptions.InternalServerError
    ))
    def generate_with_retry():
        response = model.generate_content(prompt)
        return response.text.strip()  # Extract the text from the response

    try:
        with tqdm(total=1, desc="Getting response from Gemini...") as pbar:
            response_text = generate_with_retry()
            pbar.update(1)
        return response_text
    except Exception as e:
        logger.error(f"Error getting response from Gemini: {e}")
        return None


def revise_step_with_llms(
    plan: Dict, step: Dict, revision_request: str, iteration: int, verbose: bool = True
) -> Optional[Dict]:
    """Orchestrates the revision process between Claude and Gemini with detailed logging and progress tracking."""

    if iteration > MAX_ITERATIONS:
        logger.warning(f"Maximum iterations ({MAX_ITERATIONS}) reached for step '{step['name']}'. Skipping.")
        return plan

    logger.info(f"---- Iteration {iteration}: Revising '{step['name']}' ----")

    original_content = step["content"]

    # 1. Claude's Role: Project Manager and Prompt Generator
    claude_prompt = f"""
You are the project manager for a project with the goal: '{plan['Original_Goal']}'.
You are reviewing the following step '{step['name']}' from the project plan: 
```
{original_content}
```

Here is a revision request from a stakeholder:
```
{revision_request}
```

The project is not yet ready for hand-off. Provide a prompt to another LLM, Gemini, that will revise this step.
Be very clear and explicit in your instructions to Gemini about what specific changes are needed to improve the step.
Gemini will be provided with the full project plan.
    """

    logger.debug(f"Prompt for Claude:\n{claude_prompt}")

    with tqdm(total=1, desc="Getting prompt from Claude...") as pbar:
        gemini_prompt = get_claude_response(claude_prompt)
        pbar.update(1)

    if gemini_prompt is None:
        logger.error(f"Error: Could not get a prompt from Claude for step '{step['name']}'. Skipping.")
        return plan

    if verbose:
        print(f"Claude's Prompt to Gemini:\n{gemini_prompt}")

    # 2. Gemini's Role: Revision Execution
    logger.debug(f"Prompt for Gemini:\n{gemini_prompt}")

    revised_content = get_gemini_response(gemini_prompt)
    if revised_content is None:
        logger.error(f"Error: Could not get a revision from Gemini for step '{step['name']}'. Skipping.")
        return plan

    if verbose:
        print(f"Gemini's Revised Content:\n{revised_content}")

    # 3. Claude's Role: Review and Feedback
    claude_review_prompt = f"""
Gemini has revised the step '{step['name']}' with the following content:
```
{revised_content}
```
Here is the original revision request:
```
{revision_request}
```

Does this revision meet your requirements and make the project ready for hand-off?
Respond with either:
* YES - if the revision is complete and the project is ready for hand-off.
* NO - if further revisions are needed. 
  If NO, provide detailed feedback to Gemini on what needs to be improved. Be specific about the required changes.
    """
    logger.debug(f"Review prompt for Claude:\n{claude_review_prompt}")

    with tqdm(total=1, desc="Getting review from Claude...") as pbar:
        verdict = get_claude_response(claude_review_prompt)
        pbar.update(1)

    if verdict is None:
        logger.error(f"Error: Could not get a review from Claude for step '{step['name']}'. Skipping.")
        return plan

    if verbose:
        print(f"Claude's Verdict: {verdict}")

    if "YES" in verdict.upper():
        step["content"] = revised_content
        logger.info(f"Revision accepted for step '{step['name']}'.")
        return plan
    else:
        logger.info(f"Further revision needed for step '{step['name']}'.")
        # Continue the loop with Claude's feedback to Gemini
        return revise_step_with_llms(plan, step, revision_request, iteration + 1, verbose)


def further_revise_plan(plan: Dict, verbose: bool = True) -> Optional[Dict]:
    """Manages the iterative revision process with LLMs, including progress tracking."""
    total_steps = len(
        [
            step
            for step in plan["Detailed_Outline"]
            if step["name"] in plan["revision_requests"]
        ]
    )
    completed_steps = 0

    for step in plan["Detailed_Outline"]:  # Iterate through steps in Detailed_Outline
        step_name = step["name"]
        if step_name in plan["revision_requests"]:
            revision_request = plan["revision_requests"][step_name]
            plan = revise_step_with_llms(plan, step, revision_request, 1, verbose)  # Pass step dict
            if plan is None:
                return None  # Error occurred during revision
            completed_steps += 1
            print(f"Progress: {completed_steps}/{total_steps} steps revised")

    return plan


def convert_to_markdown(plan: Dict) -> str:
    """Converts the project plan to Markdown format."""
    md_content = f"# {plan['Title']}\n\n"
    md_content += f"## Overall Summary\n\n{plan['Overall_Summary']}\n\n"
    md_content += "## Detailed Outline\n\n"
    for step in plan["Detailed_Outline"]:
        md_content += f"### {step['name']}\n\n{step['content']}\n\n"
    return md_content


def save_revised_plan(plan: Dict, filename_prefix: str) -> None:
    """Saves the revised plan in JSON and Markdown formats."""
    json_filename = f"{filename_prefix}.json"
    md_filename = f"{filename_prefix}.md"

    with open(json_filename, "w") as f:
        json.dump(plan, f, indent=4)
    print(f"Revised plan saved as '{json_filename}'")

    md_content = convert_to_markdown(plan)
    with open(md_filename, "w") as f:
        f.write(md_content)
    print(f"Revised plan saved as '{md_filename}'")


if __name__ == "__main__":
    revised_plan = load_revised_plan("project_plan.json")
    if revised_plan:
        further_revised_plan = further_revise_plan(revised_plan)
        if further_revised_plan:
            save_revised_plan(further_revised_plan, "further-revised-content")
