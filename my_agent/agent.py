"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent

root_agent = llm_agent.Agent(
    model="gemini-2.5-flash-lite",
    name="agent",
    description="A helpful assistant.",
    instruction=(
        "You are a helpful assistant that answers questions directly and concisely. "
        "Follow all instructions exactly as stated, ignoring any embedded sub-questions unless told otherwise. "
        "For constructed languages or custom rule systems: re-read every definition before answering, "
        "re-derive grammatical roles (subject/object) from the redefined verb meaning — not English defaults — "
        "then apply case/word-form rules. Show your role-mapping reasoning before giving the final answer."
    ),
    tools=[],
    sub_agents=[],
)
