# agents/data_agents.py
from openai import Agent, function_tool
from tools import drive_tools, sheets_tools, processing_tools
import pandas as pd
import io
from tools.drive_tools import list_drive_files, download_drive_file, upload_to_drive
from tools.sheets_tools import write_to_sheets
from tools.processing_tools import run_dataframe_query, run_pandas_code

import os
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

model = os.getenv("MODEL")
api_key = os.getenv("GEMINI_API_KEY")

# Handles Google Drive + Sheets
drive_agent = Agent(
    name="DriveAgent",
    instructions="""
    You manage files between Google Drive and Google Sheets.
    Use this agent when the user asks about files, uploads, or sheet updates.
    """,
    model=LitellmModel(model=model, api_key=api_key),
    tools=[list_drive_files, download_drive_file, upload_to_drive, write_to_sheets],
)

# Handles dataframe analysis
data_agent = Agent(
    name="DataAnalysisAgent",
    instructions="""
    You analyze datasets (Excel/CSV).
    You can answer natural language queries or run Pandas code on dataframes.
    """,
    model=LitellmModel(model=model, api_key=api_key),
    tools=[run_dataframe_query, run_pandas_code],
)
