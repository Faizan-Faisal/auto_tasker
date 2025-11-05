# config/settings.py
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import gspread
import os

# --- FOLDER ID (your working folder in Drive) ---
FOLDER_ID = "1ghMkHLZOpuaS5495864092JbttDSg408R5"

# --- Scopes ---
SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
]

# --- Path to your Google Service Account JSON ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, "secrets", "google_console_secrets.json")

# --- Credentials ---
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# --- Google Services (shared across project) ---
drive_service = build("drive", "v3", credentials=creds)
gc = gspread.authorize(creds)
