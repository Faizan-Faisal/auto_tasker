# agents/data_analysis_agent.py
from agents import Agent
from tools import processing_tools

import os
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

model = os.getenv("MODEL")
api_key = os.getenv("GEMINI_API_KEY")

DataAnalysisAgent = Agent(
    name="DataAnalysisAgent",
    instructions="""
    You analyze tabular data (from Excel or Sheets).
    - Use run_pandas_query for filtering, grouping, aggregations
    - Return results as structured JSON
    If the user requests charts, hand off to VisualizationAgent.
    If the user requests reports, hand off to ReportAgent.
    """,
    model=LitellmModel(model=model, api_key=api_key),
    tools=[processing_tools.run_pandas_query],
    handoffs=["VisualizationAgent", "ReportAgent"]
)
