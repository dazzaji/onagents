# When Agents Conduct Transactions

From a business, legal, and technical perspective, there's no more important LLM agent activity than conducting transactions. As someone deeply involved in crafting the Uniform Electronic Transactions Act (UETA) and a long-time advocate for responsible AI development, I'm struck by how much the world has changed since those UETA drafting meetings. We were grappling with e-commerce back then, but little did we know our work would be so remarkably prescient for today's LLM agents 25 years later.

## Key Terms and Definitions

Before diving into the infrastructure and frameworks that enable AI agent transactions, it's essential to understand a few key terms and concepts:

### Core Concepts
* **AI Agent:** The technology program that autonomously performs tasks and interacts with third parties, in this context, including use of Large Language Models (LLMs)
* **AI Agent System:** The AI agent technology plus the technology provider who operates the agent and acts as an intermediary, forming a legal agency relationship with the user
* **Agent (Legal):** A person or entity authorized to act on behalf of another (the principal)
* **Principal (Legal):** The person or entity for whom an agent acts and who exercises principal authority, some of which can be delegated to the agent
* **Third Party (Legal):** Any person who is a counter-party in a transaction with the agent who is acting on behalf of the principal
* **Contract:** A legally binding agreement between two or more parties
* **Electronic Contract (UETA):** A contract formed through electronic means
* **Human:** A natural person
* **Organization:** A legal entity, such as a corporation, business, or government agency (also known legally as an "artificial person")

### Legal Definitions from UETA
* **Transaction:** "'Transaction' means an action or set of actions occurring between two or more persons relating to the conduct of business, commercial, or governmental affairs." (UETA § 2(16))
* **Person:** "'Person' means an individual, corporation, business trust, estate, trust, partnership, limited liability company, association, joint venture, governmental agency, public corporation, or any other legal or commercial entity." (UETA § 2(12))
* **Electronic Signature:** "'Electronic signature' means an electronic sound, symbol, or process attached to or logically associated with a record and executed or adopted by a person with the intent to sign the record." (UETA § 2(8))
* **Automated Transaction:** (Defined in detail in Legal Framework section below)
* **Electronic Agent:** (Defined in detail in Legal Framework section below)

### Digital Identity Concepts
* **Digital Identity (Wyoming):** The intangible digital representation of, by and for a  person, over which they have principal authority and through which they intentionally communicate or act. Can be:
  * **Personal Digital Identity:** For individuals
  * **Organizational Digital Identity:** For legal entities
  (See WY Stat. § 8-1-102(a)(xviii-xix) (2022))
* **Attribution:** The process of establishing that an action or communication originated from a specific person or entity
* **Impersonation:** The act of falsely representing oneself as another person or entity, especially in a digital context.  Doing so to commit a crime or fraud carries specific penalties.

## Building the Legal Infrastructure: A Bridge to the Future

While use of AI agents is undeniably a novel situation for almost all people at this moment in history, there is an all-but-forgotten existing legal framework that nicely supports and reflects use of this technology, including for transactions.

Back in the late 1990s, I spent nearly two years in drafting meetings for Uniform Electronic Transactions Act (UETA), attending every session but one. During this time, we were grappling with how to create a legal framework that could adapt to the rapid evolution of technology and support the rise of e-commerce. I also co-chaired the American Bar Association group that advised on electronic agents provisions and later testified before Congress on related federal legislation (the E-SIGN Act).

The legal infrastructure we built—UETA and the federal Electronic Signatures in Global and National Commerce Act (E-SIGN)—is like a massive, invisible 50-lane highway bridge supporting today's digital economy. We designed it with the future in mind, anticipating "lanes" for autonomous agents long before the technology existed. Those seemingly excessive "lanes" are now proving essential.

Well, we suddenly need that bridge to traverse a slightly different type of traffic. Now that we finally have tons of autonomous agents and many people want to deploy them, UETA is like that bridge with perfectly suited lanes for autonomous traffic. Those wide shoulder lanes that have been gathering dust for 25 years are exactly what we need for LLM agents conducting transactions for people and organizations. They just didn't know it!

## The Legal Framework: UETA and Electronic Agents

UETA provides explicit provisions for electronic agents to conduct transactions autonomously. The law defines several key concepts that are remarkably relevant to today's AI landscape:

### Core Definitions

> **Electronic Agent:** "'Electronic agent' means a computer program or an electronic or other automated means used independently to initiate an action or respond to electronic records or performances in whole or in part, without review or action by an individual." (UETA § 2(6))

> **Automated Transaction:** "'Automated transaction' means a transaction conducted or performed, in whole or in part, by electronic means or electronic records, in which the acts or records of one or both parties are not reviewed by an individual in the ordinary course in forming a contract, performing under an existing contract, or fulfilling an obligation required by the transaction." (UETA § 2(2))

### Attribution and Legal Effect

The most important concept from these frameworks is attribution. Automated systems that ensure clear attribution to responsible legal persons help avoid an accountability gap for potential harm and damage these systems could cause. The federal ESIGN Act states that electronic agent actions are legally valid "so long as the action of any such electronic agent is legally attributable to the person to be bound." UETA offers further guidance:

> "An electronic record or electronic signature is attributable to a person if it was the act of the person. The act of the person may be shown in any manner, including a showing of the efficacy of any security procedure applied to determine the person to which the electronic record or electronic signature was attributable." (UETA § 9)

Just as vehicles are required to have clearly visible license plates when they enter upon public roads, we need appropriate measures for attribution of the acts of automated and autonomous systems back to responsible parties.

## The Iron Triangle: Principal, Agent, and Third Party

The relationships between users and their AI agents and external parties forms what I call the "iron triangle" of roles:

<img width="440" alt="Screenshot 2024-11-22 at 11 13 48 AM" src="https://github.com/user-attachments/assets/f191e752-44e4-4c54-bda5-177498ba70c9">

1. **The Principal** (the user/consumer/employee)
2. **The Agent** (the intermediary providing the AI agent tech for the Principal/user)
3. **Third Parties** (companies or other entities the AI agent interacts with)

The term “agent” itself can cause confusion, holding different meanings in the realms of software development and law. In software, it broadly refers to systems that perform tasks on behalf of users. However, the legal definition is much more specific, encompassing obligations that AI systems alone cannot fulfill.
According to the Restatement (Second) of Agency § 1(1) (1958), agency is defined as “the fiduciary relation which results from the manifestation of consent by one person to another that the other shall act on his behalf and subject to his control, and consent by the other so to act.” 

That definition might leave you scratching your head! Let's break it down. In simpler terms, 'agency' means one person agrees to act for another, like a personal assistant handling tasks for their boss. It's about a relationship built on trust, where the 'agent' is loyal to the 'principal' and follows their instructions.  The three fundamental roles, legally, are the principal, the agent, and third parties, with whom the agent interacts on behalf of the principal to get tasks done.  You can think of these three roles as a kind of iron triangle. Fiduciary duties owed by agents to principals, like the duty of loyalty, ensure the agent is legally obligated to act in the principal's best interests.  I want to emphasize that both individuals (like in our role as consumers) as well as organizations (operating through employees) using AI agent systems would be wise to prioritize working with fiduciary providers and operators of AI Agent Systems.  

Now, consider this legal concept in the context of today’s rapidly evolving AI landscape. AI agents, particularly those powered by large language models (LLMs), are quickly becoming more sophisticated and widely deployed. They’re handling increasingly complex tasks for their users, including making purchases, managing finances, and even making significant decisions with real-world consequences. However, the current models governing these AI-powered interactions are often murky and lack clarity regarding the roles, responsibilities, and legal relationships between all the players involved. This lack of clarity creates uncertainty and potential risks for both consumers and businesses, hindering the widespread adoption and beneficial potential of these powerful tools.

When you rely upon an AI Agent to conduct transactions for you which involve your duty to pay and that form other legal obligations, you should confirm that you are in fact the principal and the provider of the technology has not arrogated the role of principal to itself, leaving you as a user of their system who is relegated to operate under their principal authority.  Arguably, the entire framework of hundreds of years of agency law and practice exists to support and advance precisely such relationships of trust and reliance.  It is not only reasonable, but recommended, that these frameworks be applied to AI agent intermediated transactons as well, in order to ensure alignment with the user's interests and expected legal and business relationships and results.

To address this challenge, we can apply the robust legal framework of agency to structure the unique context of AI Agent Systems. By clarifying the roles and relationships of each party involved – the consumer or employee as principal, the intermediary that provides the AI as a tool as Agent– we can create a model that fosters trust, predictability, and accountability. The role of the intermediary combined with the AI Agent can be called an "AI Agent System."  This allows us to build on the iron triangle of agency, leveraging hundreds of years of well-understood precedent.  This approach not only provides principals with greater certainty but also empowers third-parties to engage in AI-powered interactions with greater confidence and clarity, unlocking the tremendous benefits of this technology for all.

This structure should be supported by five critical levels of system design:

1. **Governance**: Rules and bylaws ensuring transparency and accountability
2. **Data Stewardship**: Protection and ethical use of consumer data
3. **Instructions & Tooling**: Mechanisms to control and direct agent actions
4. **Agent-to-Agent Communication**: Secure interaction protocols (mostly coming soon)
5. **Identity & Payments**: Secure verification and transaction processing

## Key Considerations for Agent Transactions

### Confidentiality and Data Protection

Within the fiduciary model, robust data protection is paramount. The AI Agent System provider has a high duty of care and loyalty to the user, which includes maintaining strict confidentiality of their private information and commercial transactions. This reinforces the trust essential for users to reasonably rely upon AI agents to manage sensitive tasks.

### Security and Error Prevention

LLM agents may make unexpected errors when conducting automated transactions. UETA provides a framework for addressing these very issues through specific mechanisms for error prevention and correction.  For example:

- Security procedures can establish spending limits
- Error detection mechanisms can trigger alerts
- Failed security procedures may provide grounds for transaction reversal

### Fiduciary Duty and Trust

The most compelling use case for AI Agent Systems is their ability to act as fiduciaries, prioritizing user interests above all else.  The party providing the AI Agent technology to users, in this context, also forms a legal principal-agent relationship with that user. These agents can be bound by a "duty of loyalty" to their users, creating a trustworthy foundation for autonomous transactions. This fiduciary approach is especially important in the context of transactions, where financial and legal ramifications can be significant.

## Parallel Tracks: Individuals and Organizations

These principles apply equally to individuals and organizations using LLM agents. The Wyoming Digital Identity Act provides a framework for recognizing and managing digital identities, further strengthening the legal foundation for AI agent transactions. The Act recognizes this duality:

> **Personal Digital Identity:** "the intangible digital representation of, by and for a natural person...over which he has principal authority" (WY Stat. § 8-1-102(a)(xviii) (2022))

> **Organizational Digital Identity:** "the intangible digital representation of, by and for a corporation, business trust...or any other legal or commercial entity...over which it has principal authority" (WY Stat. § 8-1-102(a)(xix) (2022))

The Act provides strong protections against impersonation, including injunctive relief and the potential for triple damages:

> "Any person with a personal or organizational digital identity may proceed by suit to enjoin the use of any impersonations...and may require the defendants to pay to such person all profits derived from or all damages suffered by reason of such wrongful use...the court, in its discretion, may enter judgment for an amount not to exceed three (3) times any profits or damages and reasonable attorneys' fees..." (WY Stat. § 40-30-103 (2022))

Wyoming statute provides crisp clarity on these specific points, but every state of the US has legal frameworks that can be used in combinations to achieve the same results.  While the legal foundations are in place, the field of AI agent transactions is rapidly evolving. Recent developments highlight the growing momentum and practical applications of this technology.

## Recent Developments in Agent Transactions: The Stripe Agent Toolkit

The landscape of agent transactions has shifted dramatically with the recent release of Stripe's Agent Toolkit. This development, from the dominant player in online payments, is poised to accelerate the adoption of AI agents for real-world commerce. This isn't a future prediction; it's happening right now. Stripe's massive reach means this technology will quickly become embedded within the core transactional fabric of the digital economy.

The Stripe Agent Toolkit enables developers to integrate Stripe's powerful financial services directly into agentic workflows, empowering agents to not just *facilitate* transactions but to actively *participate* in them through secure, controlled mechanisms built on Stripe's robust financial infrastructure.

### Key Capabilities

1. **Creating and Managing Stripe Objects**  
   Agents can now programmatically create payment links, manage products and prices, generate invoices, and handle other essential Stripe objects. This streamlines payment workflows and automates key business processes.
   
   *Use Cases:*
   - Generating dynamic payment links for e-commerce purchases
   - Creating and managing invoices for freelancers
   - Automating product catalog management
   - Streamlining customer support workflows

2. **Metered Billing (Usage-Based Billing)**  
   Businesses can easily implement usage-based pricing for their agent services, tracking and charging customers based on metrics like token counts or execution time. This opens up new possibilities for monetizing AI agent platforms.
   
   *Use Cases:*
   - Billing for chatbot usage (messages or tokens)
   - Charging for API calls
   - Tracking and billing agent execution time
   - Usage-based pricing for AI services

3. **Online Purchasing with Stripe Issuing**  
   Perhaps the most transformative capability, agents can now generate single-use virtual cards to make purchases online. This eliminates the need for consumers to share their primary card details with multiple merchants, significantly enhancing security while streamlining procurement processes.
   
   *Use Cases:*
   - Automating travel booking with controlled spending limits
   - Managing company expenses through virtual cards
   - Dynamically managing ad campaign budgets
   - Secure online purchasing with transaction-specific cards

### Technical Implementation

The toolkit is designed for broad compatibility and ease of integration:

- **Framework Support:** Native support for popular agent frameworks including LangChain, CrewAI, and Vercel's AI SDK
- **Language Options:** Available in both Python and TypeScript
- **LLM Compatibility:** Works with any LLM provider that supports function calling
- **Security Controls:** Fine-grained access control through configurable actions
- **Error Prevention:** Built-in safeguards and monitoring capabilities

Stripe is known for its excellent developer documentation and support, making the integration process even smoother. For detailed implementation guidance, the [Stripe documentation](https://docs.stripe.com/agents) provides comprehensive examples and best practices.

### Integration Examples

Here are two practical examples of how the Stripe Agent Toolkit enables sophisticated transaction scenarios:

#### Consumer Purchase via Intermediary Service

A consumer uses a shopping agent service to find and purchase products. The agent searches for the best deals, and upon consumer approval, completes the purchase using a virtual card issued by Stripe through the intermediary service.

*Key Components:*
- Consumer-facing interface (app/website)
- AI shopping agent powered by LLMs
- Stripe Agent Toolkit integration
- Virtual card issuance for secure purchases
- Order tracking and fulfillment

#### Employee Procurement System

An employee uses a company-provided procurement tool (powered by an LLM agent) to purchase office supplies. The agent identifies approved vendors and products, and after employee confirmation, completes the purchase using a virtual card issued by Stripe.

*Key Components:*
- Company intranet/procurement portal
- AI procurement agent with policy enforcement
- Stripe Agent Toolkit integration
- Automated budget tracking and reporting
- Integration with accounting systems

These developments represent a significant step forward in making agent transactions practical and secure for both consumers and businesses. The Stripe Agent Toolkit provides the crucial infrastructure needed to bridge the gap between AI agents and real-world financial transactions.

### Perplexity's Direct-to-Consumer Shopping Agent

Just days after Stripe's announcement, Perplexity introduced a new AI-powered ecommerce feature called "Buy with Pro," marking another significant milestone in agent transactions. While Stripe enables developers to build agent-powered commerce solutions, Perplexity is taking a direct-to-consumer approach, offering U.S. Pro users the ability to purchase items through their AI agent without visiting retailer websites.

### Key Features of "Buy with Pro"

- **One-Click Checkout:** Users can store their billing and shipping information securely within Perplexity, enabling them to complete purchases with a single click. This streamlined process includes automatic tax calculations based on the user's address.  Unlike the Stripe agent API, this new Perplexity shopping agent is provided direct-to-consumer by Perplexity itself, and it will conduct the transaction on behalf of the user including handling payment.

Here are the key business components of this new agent transaction service:
  
- **Free Shipping:** Pro subscribers benefit from free shipping on all purchases made through the "Buy with Pro" feature.

- **Visual Product Cards:** For shopping-related queries, Perplexity displays visual cards that provide detailed product information, including pricing, seller details, and pros and cons. These cards are designed to offer unbiased recommendations without sponsored content.

- **Snap to Shop:** This visual search tool allows users to upload a photo of a product they are interested in. Perplexity then identifies and displays similar items available for purchase, enhancing the shopping experience even when users lack specific product names or descriptions.

- **Integration with Shopify:** By integrating Shopify's API, Perplexity gains access to a wide range of products and merchants, allowing it to provide comprehensive shopping options directly within its platform.

This new feature positions Perplexity as a competitor to major ecommerce platforms like Amazon and Google Shopping by offering a seamless shopping experience directly through its AI search engine. The company is currently focusing on growing its search query volume rather than monetizing this feature immediately, with advertising business remaining the primary revenue stream focus.

### The Inflection Point

Between the Stripe Agent API and Perplexity's shopping agent both launching within the last week (as of November 20, 2024), it is clear that transactional AI agents are no longer a future possibility but have reached broad scale availability. These complementary approaches - Stripe's developer toolkit and Perplexity's direct-to-consumer service - demonstrate how quickly this technology is being commercialized and made available at population-scale.


## The Future of Agent Transactions

As transactional AI agent technology matures, two key areas (among others) that will shape its evolution are:

1. The development of common protocols for agent-to-agent communication, enabling seamless and efficient automated transactions
2. Sophisticated mechanisms for managing the delegation of authority from the principal user to the AI agent, balancing automation with user control

This will ensure that agents act within clearly defined boundaries while maximizing their utility. The foundation we laid with UETA has proven remarkably prescient, providing crucial guardrails for responsible innovation while protecting user interests. The challenge now is to build upon this foundation, creating systems that maintain trust while unleashing the transformative potential of autonomous agents.

---

*For more detailed discussion of zero-knowledge proofs and other emerging legal considerations for AI agents, standby for an upcoming whitepaper I'm co-authoring with Diana Stern: ["From Fine Print to Machine Code: How AI Agents are Rewriting the Rules of Engagement"*

-------

Further thoughts and context on AI agent transactions: [https://youtu.be/5xneAPUfueg](https://youtu.be/5xneAPUfueg) 

<iframe width="560" height="315" src="https://www.youtube.com/embed/5xneAPUfueg?si=EyycAw1dljz15tr7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
