# from agents import Agent, function_tool
# import pandas as pd
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
# from reportlab.lib.styles import getSampleStyleSheet

# @function_tool
# def create_pdf_report(dataframe: dict, filename: str = "report.pdf") -> str:
#     """Generate a PDF report summarizing a DataFrame."""
#     df = pd.DataFrame(dataframe["data"], columns=dataframe["columns"])
#     doc = SimpleDocTemplate(filename)
#     styles = getSampleStyleSheet()
#     elements = [Paragraph("Data Report", styles["Title"])]

#     # Add table
#     table_data = [df.columns.tolist()] + df.values.tolist()
#     elements.append(Table(table_data))
    
#     doc.build(elements)
#     return filename


# tools/report_tools.py

from agents import function_tool
from pydantic import BaseModel, Field
from typing import List
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import base64


class ReportSection(BaseModel):
    """A section in the report with a title and content."""
    title: str = Field(..., description="The title of the section")
    content: str = Field(..., description="The text content of the section")


class ReportData(BaseModel):
    """Structured report data."""
    title: str = Field(..., description="Main report title")
    author: str = Field(..., description="Author of the report")
    sections: List[ReportSection] = Field(..., description="List of sections in the report")


@function_tool
def create_pdf_report(data: ReportData) -> str:
    """
    Creates a PDF report based on the given structured data.
    Args:
        data: A ReportData object containing title, author, and sections.
    Returns:
        A base64-encoded string of the generated PDF.
    """
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, data.title)

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 70, f"Author: {data.author}")

    y = height - 100
    for section in data.sections:
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, section.title)
        y -= 20
        c.setFont("Helvetica", 12)
        for line in section.content.split("\n"):
            c.drawString(60, y, line)
            y -= 15
        y -= 10
        if y < 100:
            c.showPage()
            y = height - 50

    c.save()
    buffer.seek(0)

    encoded_pdf = base64.b64encode(buffer.read()).decode("utf-8")
    return encoded_pdf
