# tools/drive_tools.py
from agents import function_tool
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from config.settings import drive_service, FOLDER_ID
from pydantic import BaseModel
import io, os

class DriveFile(BaseModel):
    id: str
    name: str
    mimeType: str | None = None

class DriveFileList(BaseModel):
    files: list[DriveFile]

class FileUploadResponse(BaseModel):
    id: str

class FileDownloadResponse(BaseModel):
    filename: str


@function_tool
async def list_files(query: str | None = None, page_size: int = 20) -> DriveFileList:
    """List files inside the configured Google Drive folder."""
    print("🔍 LIST FILES")
    # Always default to your folder if no query provided
    if query is None:
        query = f"'{FOLDER_ID}' in parents"

    try:
        results = drive_service.files().list(
            q=query,
            pageSize=page_size,
            fields="files(id, name, mimeType)"
        ).execute()

        file_list = results.get("files", [])
        files = [DriveFile(**f) for f in file_list]

        print(f"DEBUG LIST FILES → Found {len(files)} items")
        for f in files:
            print(f"  - {f.name} ({f.id})")

        return DriveFileList(files=files)

    except Exception as e:
        print("❌ ERROR in list_files:", e)
        raise


@function_tool
async def download_file(file_id: str, filename: str, save_dir: str = "downloads") -> FileDownloadResponse:
    """Download a Google Drive file by ID."""
    
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, filename)

    try:
        request = drive_service.files().get_media(fileId=file_id)
        with io.FileIO(save_path, "wb") as fh:
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                _, done = downloader.next_chunk()

        print(f"Downloaded → {save_path}")
        return FileDownloadResponse(filename=save_path)

    except Exception as e:
        print("❌ ERROR in download_file:", e)
        raise


@function_tool
async def upload_file(filename: str, new_name: str, convert_to_sheet: bool = False, folder_id: str | None = None) -> FileUploadResponse:
    """Upload a file to Google Drive."""
    
    folder_id = folder_id or FOLDER_ID

    file_metadata = {
        "name": new_name,
        "parents": [folder_id],
    }

    if convert_to_sheet:
        file_metadata["mimeType"] = "application/vnd.google-apps.spreadsheet"

    try:
        media = MediaFileUpload(filename)

        uploaded = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id"
        ).execute()

        print(f"Uploaded → {uploaded.get('id')}")
        return FileUploadResponse(id=uploaded.get("id"))

    except Exception as e:
        print("❌ ERROR in upload_file:", e)
        raise
