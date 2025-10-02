"""
Central registry for all project tools.
"""

from .drive_tools import list_files, download_file, upload_file
from .sheets_tools import read_sheet, write_sheet
from .processing_tools import run_pandas_query
from .visualization_tool import generate_chart
from .report_tools import create_pdf_report

# Tool registry dictionary for structured access
TOOLS = {
    "list_files": list_files,
    "download_file": download_file,
    "upload_file": upload_file,
    "read_sheet": read_sheet,
    "write_sheet": write_sheet,
    "run_pandas_query": run_pandas_query,
    "generate_chart": generate_chart,
    "create_pdf_report": create_pdf_report,
}

__all__ = [
    "list_files",
    "download_file",
    "upload_file",
    "read_sheet",
    "write_sheet",
    "run_pandas_query",
    "generate_chart",
    "create_pdf_report",
    "TOOLS",
]
