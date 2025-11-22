# agents/drive_agent.py
from agents import Agent
from tools.drive_tools import list_files, download_file, upload_file

import os
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from config.settings import FOLDER_ID

model = os.getenv("MODEL")
api_key = os.getenv("GEMINI_API_KEY")


DriveAgent = Agent(
    name="DriveAgent",
    instructions="""
    You are DriveAgent.
    Your job is to call relevated tools and return the results in json format.
    {"results": "<Results of the tool or null>",
    "tool_name": "<Name of the tool or null>"}
    
    RULES:
    - If user requests listing → call list_files and list all the files from the google drive folder.
    - If user requests downloading → call download_file and download the file from the google drive folder.
    - If user requests uploading → call upload_file and upload the file to the google drive folder.     
    - ALWAYS call a tool. NEVER ask questions.
    # - Respond ONLY using tool calls.
    """,
    model=LitellmModel(model=model, api_key=api_key),
    tools=[list_files, download_file, upload_file],
    handoffs=["DataAnalysisAgent"]
)
