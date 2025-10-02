# agents/supervisor_agent.py
from agents import Agent

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
    handoffs=["DriveAgent", "SheetsAgent", "DataAnalysisAgent", "VisualizationAgent", "ReportAgent"]
)
