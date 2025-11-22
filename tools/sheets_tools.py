# tools/sheets_tools.py
from agents import function_tool
from config.settings import gc
from pydantic import BaseModel
import pandas as pd

class SheetData(BaseModel):
    columns: list[str]
    data: list[list]

class SheetWriteResponse(BaseModel):
    message: str


@function_tool
async def read_sheet(sheet_id: str, worksheet: int = 0) -> SheetData:
    """Read a Google Sheet into a DataFrame-like dict (columns + data)."""
    sh = gc.open_by_key(sheet_id)
    ws = sh.get_worksheet(worksheet)
    data = ws.get_all_records()
    df = pd.DataFrame(data)
    return SheetData(columns=df.columns.tolist(), data=df.values.tolist())


@function_tool
async def write_sheet(sheet_id: str, dataframe: SheetData, worksheet: int = 0) -> SheetWriteResponse:
    """Write a DataFrame-like dict (columns + data) back to Google Sheet."""
    sh = gc.open_by_key(sheet_id)
    ws = sh.get_worksheet(worksheet)
    ws.clear()
    df = pd.DataFrame(dataframe.data, columns=dataframe.columns)
    ws.update([df.columns.values.tolist()] + df.values.tolist())
    return SheetWriteResponse(message="✅ Sheet updated successfully")
