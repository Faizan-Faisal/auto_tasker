# agents/drive_agent.py
from agents import Agent
from tools import drive_tools

DriveAgent = Agent(
    name="DriveAgent",
    instructions="""
    You manage Google Drive files.
    - Use list_files to find files
    - Use download_file for Excel files
    - Use upload_file to save processed results back to Drive
    If the user requests data analysis, hand off to DataAnalysisAgent.
    """,
    tools=[drive_tools.list_files, drive_tools.download_file, drive_tools.upload_file],
    handoffs=["DataAnalysisAgent"]
)
