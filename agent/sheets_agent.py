# agents/sheets_agent.py
from agents import Agent
from tools import sheets_tools

import os
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

model = os.getenv("MODEL")
api_key = os.getenv("GEMINI_API_KEY")

SheetsAgent = Agent(
    name="SheetsAgent",
    instructions="""
    You manage live Google Sheets.
    - Use read_sheet to fetch sheet content
    - Use write_sheet to update a sheet
    If deeper analysis is needed, hand off to DataAnalysisAgent.
    """,
    model=LitellmModel(model=model, api_key=api_key),
    tools=[sheets_tools.read_sheet, sheets_tools.write_sheet],
    handoffs=["DataAnalysisAgent", "VisualizationAgent"]
)
