# agents/drive_agent.py
from agents import Agent
from tools import drive_tools

import os
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

model = os.getenv("MODEL")
api_key = os.getenv("GEMINI_API_KEY")

DriveAgent = Agent(
    name="DriveAgent",
    instructions="""
    You manage Google Drive files.
    - Use list_files to find files
    - Use download_file for Excel files
    - Use upload_file to save processed results back to Drive
    If the user requests data analysis, hand off to DataAnalysisAgent.
    """,
    model=LitellmModel(model=model, api_key=api_key),
    tools=[drive_tools.list_files, drive_tools.download_file, drive_tools.upload_file],
    handoffs=["DataAnalysisAgent"]
)
