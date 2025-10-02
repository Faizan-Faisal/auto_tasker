# tools/drive_tools.py
from agents import function_tool, RunContextWrapper
from typing_extensions import Any
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from config.settings import drive_service
import io


@function_tool
async def list_files(query: str | None = None, page_size: int = 10) -> list[dict]:
    """List files from Google Drive with an optional query filter."""
    results = drive_service.files().list(
        q=query,
        pageSize=page_size,
        fields="files(id, name, mimeType)"
    ).execute()
    return results.get("files", [])


@function_tool
async def download_file(file_id: str, filename: str) -> str:
    """Download a file from Google Drive given its file ID."""
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(filename, "wb")
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return filename


@function_tool
async def upload_file(filename: str, new_name: str, convert_to_sheet: bool = False) -> str:
    """Upload a file to Google Drive. Optionally convert Excel to Google Sheet."""
    file_metadata = {
        "name": new_name,
        "mimeType": "application/vnd.google-apps.spreadsheet" if convert_to_sheet else None
    }
    media = MediaFileUpload(
        filename,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    uploaded = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()
    return uploaded.get("id")
