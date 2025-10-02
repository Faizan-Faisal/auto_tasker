# agents/sheets_agent.py
from agents import Agent
from tools import sheets_tools

SheetsAgent = Agent(
    name="SheetsAgent",
    instructions="""
    You manage live Google Sheets.
    - Use read_sheet to fetch sheet content
    - Use write_sheet to update a sheet
    If deeper analysis is needed, hand off to DataAnalysisAgent.
    """,
    tools=[sheets_tools.read_sheet, sheets_tools.write_sheet],
    handoffs=["DataAnalysisAgent", "VisualizationAgent"]
)
