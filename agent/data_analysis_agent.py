# agents/data_analysis_agent.py
from agents import Agent
from tools import processing_tools

DataAnalysisAgent = Agent(
    name="DataAnalysisAgent",
    instructions="""
    You analyze tabular data (from Excel or Sheets).
    - Use run_pandas_query for filtering, grouping, aggregations
    - Return results as structured JSON
    If the user requests charts, hand off to VisualizationAgent.
    If the user requests reports, hand off to ReportAgent.
    """,
    tools=[processing_tools.run_pandas_query],
    handoffs=["VisualizationAgent", "ReportAgent"]
)
