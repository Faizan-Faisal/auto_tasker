# agents/supervisor_agent.py
from agents import Agent
import os
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

model = os.getenv("MODEL")
api_key = os.getenv("GEMINI_API_KEY")

SupervisorAgent = Agent(
    name="SupervisorAgent",
    instructions="""
    You are the orchestrator. 
    Route tasks to the correct specialized agent:
    - DriveAgent: file management
    - SheetsAgent: live Google Sheets
    - DataAnalysisAgent: Pandas queries
    - VisualizationAgent: charts
    - ReportAgent: final reports
    """,
    model=LitellmModel(model=model, api_key=api_key),
    handoffs=["DriveAgent", "SheetsAgent", "DataAnalysisAgent", "VisualizationAgent", "ReportAgent"]
)
