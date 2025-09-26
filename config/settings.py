# config/settings.py
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import gspread

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets"
]
SERVICE_ACCOUNT_FILE = "secrets/google_console_secrets.json"

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Google Services
drive_service = build("drive", "v3", credentials=creds)
gc = gspread.authorize(creds)
