# # agents/supervisor_agent.py
from agents import Agent
import os
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from tools.drive_tools import list_files, download_file, upload_file
from tools.sheets_tools import read_sheet, write_sheet
from tools.processing_tools import run_pandas_query
from tools.visualization_tool import generate_chart
from tools.report_tools import create_pdf_report
model = os.getenv("MODEL")
api_key = os.getenv("GEMINI_API_KEY")

SupervisorAgent = Agent(
    name="SupervisorAgent",
    instructions = """
    You are the SupervisorAgent. Your job is to decide which agent should handle the user's request. 
    Thus, you handoff the request to the appropriate agent.

    Execute a tool and RETURN A RESULT IN JSON OBJECT IN THE FOLLOWING FORMAT:

    {
    "handoff_to": "<AgentName>",
    "tool": "<ToolName or null>",
    "message": "<Short description of what will be done>",
    "output": "<Output of the tool or null>"
    }

   RULES:
   - agent must be one of: "DriveAgent", "SheetsAgent", "DataAnalysisAgent", "VisualizationAgent", "ReportAgent"

   """,

    model=LitellmModel(model=model, api_key=api_key),
    handoffs=["DriveAgent", "SheetsAgent", "DataAnalysisAgent", "VisualizationAgent", "ReportAgent"],
    tools=[list_files, download_file, upload_file, read_sheet, write_sheet, run_pandas_query, generate_chart, create_pdf_report]

)

# SupervisorAgent = Agent(
#     name="SupervisorAgent",
#     instructions="""
#         You are the Supervisor. Decide which agent should run the request.

#         Respond using this structure:
#         and return the results in json format.
#         {"handoff_to": "<AgentName>",
#         "results": "<Results of the tool of the handoff agent or null>"}
#         Valid agents:
#         - DriveAgent
#         - SheetsAgent
#         - DataAnalysisAgent
#         - VisualizationAgent
#         - ReportAgent
#     """,
#     model=LitellmModel(model=model, api_key=api_key),
#     handoffs=["DriveAgent", "SheetsAgent", "DataAnalysisAgent", "VisualizationAgent", "ReportAgent"]
# )
