# agents/report_agent.py
from agents import Agent
from tools import create_pdf_report

import os
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

model = os.getenv("MODEL")
api_key = os.getenv("GEMINI_API_KEY")

ReportAgent = Agent(
    name="ReportAgent",
    instructions="""
    You create final reports from analyzed data.
    Use create_pdf_report for PDF reports.
    """,
    model=LitellmModel(model=model, api_key=api_key),
    tools=[create_pdf_report]
)
