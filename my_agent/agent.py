"""
This file is where you will implement your agent.
The `root_agent` is used to evaluate your agent's performance.
"""

from google.adk.agents import llm_agent

from my_agent.tools import calculator
from my_agent.tools.read_pdf import read_pdf
from my_agent.tools.read_pdf_tables import read_pdf_tables

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
        "Answer step by step: gather data with tools first, then reason, then answer. "
        "do multistep research: search, readpage, then search again with new details you learned. Repeat."
        "If a PDF is referenced, prefer read_pdf_tables for tabular data, otherwise use read_pdf. "
        "Use the calculator for all arithmetic and counting. "
    ),
    tools=[calculator, read_pdf, read_pdf_tables],
    sub_agents=[],
)
