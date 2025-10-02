from agents import Agent, function_tool
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet

@function_tool
def create_pdf_report(dataframe: dict, filename: str = "report.pdf") -> str:
    """Generate a PDF report summarizing a DataFrame."""
    df = pd.DataFrame(dataframe["data"], columns=dataframe["columns"])
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = [Paragraph("Data Report", styles["Title"])]

    # Add table
    table_data = [df.columns.tolist()] + df.values.tolist()
    elements.append(Table(table_data))
    
    doc.build(elements)
    return filename
