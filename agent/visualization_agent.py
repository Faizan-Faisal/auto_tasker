# agents/visualization_agent.py
from agents import Agent
from tools import visualization_tool , generate_chart
import os
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

model = os.getenv("MODEL")
api_key = os.getenv("GEMINI_API_KEY")

VisualizationAgent = Agent(
    name="VisualizationAgent",
    instructions="""
    You generate charts from DataFrames.
    Use generate_chart to create visualizations.
    If the user wants these charts in a report, hand off to ReportAgent.
    """,
    model=LitellmModel(model=model, api_key=api_key),
    tools=[generate_chart],
    handoffs=["ReportAgent"]
)
