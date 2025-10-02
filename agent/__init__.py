"""
Central registry for all project agents.
"""

from .drive_agent import DriveAgent
from .sheets_agent import SheetsAgent
from .data_analysis_agent import DataAnalysisAgent
from .visualization_agent import VisualizationAgent
from .report_agent import ReportAgent
from .supervisor_agent import SupervisorAgent

# Agent registry dictionary for easy access
AGENTS = {
    "DriveAgent": DriveAgent,
    "SheetsAgent": SheetsAgent,
    "DataAnalysisAgent": DataAnalysisAgent,
    "VisualizationAgent": VisualizationAgent,
    "ReportAgent": ReportAgent,
    "SupervisorAgent": SupervisorAgent,
}

__all__ = [
    "DriveAgent",
    "SheetsAgent",
    "DataAnalysisAgent",
    "VisualizationAgent",
    "ReportAgent",
    "SupervisorAgent",
    "AGENTS",
]
