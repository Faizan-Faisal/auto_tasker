# agents/visualization_agent.py
from agents import Agent
from tools import visualization_tool

VisualizationAgent = Agent(
    name="VisualizationAgent",
    instructions="""
    You generate charts from DataFrames.
    Use generate_chart to create visualizations.
    If the user wants these charts in a report, hand off to ReportAgent.
    """,
    tools=[generate_chart],
    handoffs=["ReportAgent"]
)
