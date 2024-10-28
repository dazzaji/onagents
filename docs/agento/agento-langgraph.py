# Simple Example: Agento Design Pattern Implemented in LangGraph

import operator
import time
from typing import Annotated, List, TypedDict, Union, Optional
import os
from dotenv import load_dotenv
import re

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import END, StateGraph, START
from langgraph.checkpoint.memory import MemorySaver

# Load environment variables
load_dotenv()

# Get OpenAI API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

print("Environment variables loaded successfully...")

# Define the state for the framework
class ThoughtState(TypedDict):
    goal: str
    approaches: List[dict]
    feasibility_insights: Annotated[List[dict], operator.add]
    alignment_insights: Annotated[List[dict], operator.add]
    selected_approach: str

def print_api_interaction(direction: str, content: str):
    print("\n" + "="*80)
    print(f"{'🔵 SENDING TO API' if direction == 'send' else '🟢 RECEIVED FROM API'}:")
    print("-"*80)
    print(content)
    print("="*80 + "\n")

print("Creating LLM instance...")
# Create agents using ChatOpenAI
llm = ChatOpenAI(model="gpt-4", temperature=0.0)

def create_thinking_agent(tools=None):
    print("\n🔧 Creating thinking agent...")
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are a thinking agent that creates varied approaches to achieving goals. When generating approaches:
            1. Create exactly 3 distinct ways to achieve the goal
            2. Number each clearly as 'APPROACH 1:', 'APPROACH 2:', and 'APPROACH 3:'
            3. Make each approach detailed and actionable
            4. Organize each approach in whatever way best serves achieving the goal
               - This could be steps, parallel activities, iterative cycles, 
                 or any other organization that makes sense
               - Don't force a linear or time-based structure unless it truly fits the goal
               - Let the nature of the goal guide how the approach should be organized
            5. Format in markdown with clear headers and bullet points
            
            Focus on "what" needs to be done rather than imposing a particular organizational structure.
            The organization should emerge from the nature of the goal itself."""
        ),
        MessagesPlaceholder(variable_name="messages"),
    ])
    print_api_interaction("send", "Thinking Agent System Prompt Created")
    return prompt | llm

def create_feasibility_evaluation_agent(tools=None):
    print("\n🔧 Creating feasibility evaluation agent...")
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are an evaluation agent that assesses the feasibility of different approaches. For each approach:
            1. Provide a specific likelihood of success (0-100%)
            2. Consider practical constraints, resources needed, and potential challenges
            3. Vary your assessments based on each approach's unique characteristics
            4. Provide 2-3 sentences of specific reasoning
            5. Be critical - avoid giving every approach the same score
            
            Format your response as:
            Likelihood of Success: X%
            Reasoning: [Your specific analysis]"""
        ),
        MessagesPlaceholder(variable_name="messages"),
    ])
    print_api_interaction("send", "Feasibility Evaluation Agent System Prompt Created")
    return prompt | llm

def create_goal_alignment_evaluation_agent(tools=None):
    print("\n🔧 Creating goal alignment evaluation agent...")
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are an evaluation agent that assesses how well an approach aligns with achieving the stated goal.
            For each approach, evaluate:
            1. If this approach succeeds, will it fully achieve what was wanted?
            2. Are there aspects of the goal not addressed by this approach?
            3. Does the approach include elements not relevant to the goal?
            4. Is the approach making any unwarranted assumptions?
            
            Provide:
            1. An alignment percentage (0-100%)
            2. A categorization based on the percentage:
               - Very aligned (75-100%)
               - Partially aligned (25-74%)
               - Poorly aligned (0-24%)
            3. Clear reasoning for your evaluation
            
            Format your response as:
            Alignment Score: X%
            Category: [Very/Partially/Poorly] aligned
            Reasoning: [Your detailed analysis]
            
            Important: Focus on whether the approach will achieve the stated goal, not on whether it follows 
            any particular methodology or best practices."""
        ),
        MessagesPlaceholder(variable_name="messages"),
    ])
    print_api_interaction("send", "Goal Alignment Evaluation Agent System Prompt Created")
    return prompt | llm

print("Setting up agents...")
thinking_agent = create_thinking_agent()
feasibility_evaluation_agent = create_feasibility_evaluation_agent()
goal_alignment_evaluation_agent = create_goal_alignment_evaluation_agent()

def parse_approaches(content: str) -> List[dict]:
    """Parse the thinking agent's output into separate approaches."""
    # More comprehensive pattern to match various approach header formats
    pattern = r'(?:^|\n)(?:# |#|(?:\*\*)?)\s*APPROACH\s*\d+[\:|\.]?'
    
    print(f"\nDebug: Original content length: {len(content)} characters")
    
    # Split the content
    approaches = re.split(pattern, content, flags=re.MULTILINE)
    # Remove empty sections and clean up
    approaches = [p.strip() for p in approaches if p.strip()]
    
    print(f"Debug: Found {len(approaches)} raw sections after splitting")
    
    # Create approach dictionaries
    result = []
    for i, approach_content in enumerate(approaches, 1):
        try:
            cleaned = clean_content(approach_content)
            if cleaned:  # Only add if there's actual content
                result.append({
                    "number": i,
                    "content": cleaned
                })
                print(f"Debug: Processed approach {i} ({len(cleaned)} characters)")
        except Exception as e:
            print(f"Debug: Error processing approach {i}: {str(e)}")
    
    print(f"Debug: Successfully processed {len(result)} complete approaches\n")
    return result

def clean_content(text: str) -> str:
    """Clean markdown formatting and extra whitespace from content."""
    # Remove any remaining markdown header markers
    text = re.sub(r'^#\s*', '', text, flags=re.MULTILINE)
    
    # Remove asterisks (bold/italic markers) while preserving content
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    
    # Clean up multiple newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Clean up any extra whitespace
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(line for line in lines if line)
    
    return text.strip()

def request_goal(state):
    print("\n💭 What would you like to achieve?")
    user_input = input("Your goal: ")
    print(f"\nReceived goal: {user_input}")
    return {"goal": user_input}

def generate_approaches(state):
    print("\n🌟 Generating approaches...")
    try:
        prompt = (
            f"Consider this goal: {state['goal']}\n"
            "Propose 3 distinct approaches to achieve it. Each approach should:\n"
            "- Be organized in whatever way best serves the goal\n"
            "- Not be constrained by traditional phases or timelines\n"
            "- Allow for non-linear, parallel, or emergent activities if appropriate\n"
            "Label each as 'APPROACH 1:', 'APPROACH 2:', and 'APPROACH 3:'"
        )
        message = HumanMessage(content=prompt)
        print_api_interaction("send", f"Thinking about approaches:\n{message.content}")
        
        result = thinking_agent.invoke({"messages": [message]})
        print_api_interaction("receive", f"Generated approaches:\n{result.content}")
        
        approaches = parse_approaches(result.content)
        print(f"\n💡 Successfully generated {len(approaches)} approaches")
        return {"approaches": approaches}
    except Exception as e:
        print(f"❌ Error generating approaches: {str(e)}")
        return {"approaches": []}

def evaluate_feasibility(state):
    print("\n⚖️ Evaluating feasibility...")
    evaluations = []
    for approach in state["approaches"]:
        try:
            print(f"\n📝 Evaluating Approach {approach['number']} of {len(state['approaches'])}:")
            prompt = (
                f"Goal: {state['goal']}\n\n"
                f"Approach #{approach['number']}:\n{approach['content']}\n\n"
                "Evaluate how feasible this approach is. Consider practical constraints, "
                "resources needed, and potential challenges. Provide a specific "
                "likelihood of success and detailed reasoning."
            )
            print_api_interaction("send", f"Feasibility Evaluation Input:\n{prompt}")
            
            evaluation = feasibility_evaluation_agent.invoke(
                {"messages": [HumanMessage(content=prompt)]}
            )
            print_api_interaction("receive", f"Feasibility Evaluation Output:\n{evaluation.content}")
            
            evaluations.append({
                "approach_number": approach['number'],
                "approach_content": approach['content'],
                "evaluation": evaluation.content
            })
        except Exception as e:
            print(f"❌ Error evaluating feasibility: {str(e)}")
            evaluations.append({
                "approach_number": approach['number'],
                "approach_content": approach['content'],
                "evaluation": "Error during feasibility evaluation"
            })
    return {"feasibility_insights": evaluations}

def evaluate_goal_alignment(state):
    print("\n🎯 Evaluating goal alignment...")
    evaluations = []
    for approach in state["approaches"]:
        try:
            print(f"\n📝 Evaluating Goal Alignment for Approach {approach['number']} of {len(state['approaches'])}:")
            prompt = (
                f"Original Goal: {state['goal']}\n\n"
                f"Approach #{approach['number']}:\n{approach['content']}\n\n"
                "Evaluate how well this approach aligns with achieving the stated goal. "
                "Consider whether successful execution would fully achieve what was wanted. "
                "Provide an alignment percentage and detailed reasoning."
            )
            print_api_interaction("send", f"Goal Alignment Evaluation Input:\n{prompt}")
            
            evaluation = goal_alignment_evaluation_agent.invoke(
                {"messages": [HumanMessage(content=prompt)]}
            )
            print_api_interaction("receive", f"Goal Alignment Evaluation Output:\n{evaluation.content}")
            
            evaluations.append({
                "approach_number": approach['number'],
                "approach_content": approach['content'],
                "evaluation": evaluation.content
            })
        except Exception as e:
            print(f"❌ Error evaluating goal alignment: {str(e)}")
            evaluations.append({
                "approach_number": approach['number'],
                "approach_content": approach['content'],
                "evaluation": "Error during goal alignment evaluation"
            })
    return {"alignment_insights": evaluations}

print("Adding nodes to workflow...")
workflow = StateGraph(ThoughtState)
workflow.add_node("request_goal", request_goal)
workflow.add_node("generate_approaches", generate_approaches)
workflow.add_node("evaluate_feasibility", evaluate_feasibility)
workflow.add_node("evaluate_goal_alignment", evaluate_goal_alignment)

print("Setting up workflow edges...")
workflow.add_edge(START, "request_goal")
workflow.add_edge("request_goal", "generate_approaches")
workflow.add_edge("generate_approaches", "evaluate_feasibility")
workflow.add_edge("evaluate_feasibility", "evaluate_goal_alignment")
workflow.add_edge("evaluate_goal_alignment", END)

print("Compiling workflow...")
compiled_graph = workflow.compile()

if __name__ == "__main__":
    print("\n🚀 Initializing workflow...")
    initial_state = {
        "goal": "",
        "approaches": [],
        "feasibility_insights": [],
        "alignment_insights": [],
        "selected_approach": ""
    }
    
    try:
        start_time = time.time()
        timeout = 120  # 2 minutes timeout
        
        print("▶️ Starting execution...")
        final_state = compiled_graph.invoke(
            initial_state, 
            config={
                "checkpointer": MemorySaver(),
                "recursion_limit": 10
            }
        )
        
        print("\n" + "="*80)
        print("📊 FINAL RESULTS:")
        print("="*80)
        for i in range(len(final_state["approaches"])):
            print(f"\n🔍 APPROACH {i+1}:")
            print("-"*40)
            print("Approach Content:")
            print(final_state["approaches"][i]["content"])
            print("\nFeasibility Evaluation:")
            print(final_state["feasibility_insights"][i]["evaluation"])
            print("\nGoal Alignment Evaluation:")
            print(final_state["alignment_insights"][i]["evaluation"])
            print("-"*40)
            
        execution_time = time.time() - start_time
        print(f"\n⏱️ Total execution time: {execution_time:.2f} seconds")
        
    except KeyboardInterrupt:
        print("\n⚠️ Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        raise
    finally:
        print("\n✅ Workflow completed or terminated.")
