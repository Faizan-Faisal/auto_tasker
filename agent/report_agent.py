# agents/report_agent.py

ReportAgent = Agent(
    name="ReportAgent",
    instructions="""
    You create final reports from analyzed data.
    Use create_pdf_report for PDF reports.
    """,
    tools=[create_pdf_report]
)
