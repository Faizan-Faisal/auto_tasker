# agents/data_agents.py
from openai import Agent, function_tool
from tools import drive_tools, sheets_tools, processing_tools
import pandas as pd
import io
from tools.drive_tools import list_drive_files, download_drive_file, upload_to_drive
from tools.sheets_tools import write_to_sheets
from tools.processing_tools import run_dataframe_query, run_pandas_code

# Handles Google Drive + Sheets
drive_agent = Agent(
    name="DriveAgent",
    instructions="""
    You manage files between Google Drive and Google Sheets.
    Use this agent when the user asks about files, uploads, or sheet updates.
    """,
    tools=[list_drive_files, download_drive_file, upload_to_drive, write_to_sheets],
)

# Handles dataframe analysis
data_agent = Agent(
    name="DataAnalysisAgent",
    instructions="""
    You analyze datasets (Excel/CSV).
    You can answer natural language queries or run Pandas code on dataframes.
    """,
    tools=[run_dataframe_query, run_pandas_code],
)
