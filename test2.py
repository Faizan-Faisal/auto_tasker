from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# --- Replace this with the ID of your 'auto-tasker-folder' ---
FOLDER_ID = "1ghMkHLZOpuaS5zTVDBP2JbttDSg408R5"
# -------------------------------------------------------------

# It's good practice to use the narrowest scope
SCOPES = ['https://www.googleapis.com/auth/drive'] 
# Use 'https://www.googleapis.com/auth/drive' if you need to create/modify files

creds = Credentials.from_service_account_file("secrets/google_console_secrets.json", scopes=SCOPES)
service = build("drive", "v3", credentials=creds)

# 1. Construct the query to search within the specific folder
# 'in parents' means the file is located inside this folder ID
query = f"'{FOLDER_ID}' in parents"

# 2. Add the query (q) parameter to your list request
results = service.files().list(
    q=query,                                  # <--- The key modification
    pageSize=12, 
    fields="files(id, name)"
).execute()

items = results.get("files", [])

if not items:
    print("No files found in the specified folder.")
else:
    print("Files found in the folder:", len(items))
    for file in items:
        print(f"  {file['name']} ({file['id']})")