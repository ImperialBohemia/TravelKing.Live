#!/usr/bin/env python3
"""Push audit results to Brain (Google Sheets Audit tab)."""
import json
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

VAULT = "/home/q/TravelKing.Live/config/access_vault.json"
SA = "/home/q/TravelKing.Live/config/service_account.json"

with open(VAULT) as f:
    vault = json.load(f)

creds = service_account.Credentials.from_service_account_file(
    SA, scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
sheets = build("sheets", "v4", credentials=creds)
sheet_id = vault["travelking"]["sheet_id"]
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

audit_data = [
    ["ENTERPRISE AUDIT", timestamp, "", ""],
    ["Service", "Status", "Details", "Action"],
    ["cPanel API", "OK", "travelking.live / server707", ""],
    ["Google Service Account", "OK", "Sheets + Drive Active", ""],
    ["Gmail SMTP", "OK", "trendnatures@gmail.com", ""],
    ["GitHub", "OK", "ImperialBohemia/TravelKing.Live", ""],
    ["Travelpayouts", "OK", "API Active", ""],
    ["Bing IndexNow", "OK", "Key verified on domain", ""],
    ["Node.js App", "OK", "v20 Production | server.js", ""],
    ["Domain + SSL", "OK", "HTTPS Active", ""],
    ["", "", "", ""],
    ["SCORE", "8/8 (100%)", "ENTERPRISE READY", "FORTRESS"],
    ["", "", "", ""],
    ["VISUAL ENGINE", "", "", ""],
    ["Nano Banana Pro", "READY", "Unlimited Images (4K)", "Auto-Generate"],
    ["Imagen 4", "READY", "Text Rendering Specialist", "Auto-Generate"],
    ["Veo 3 (Video)", "RESTRICTED", "1000 credits/mo", "Manual Only"],
    ["", "", "", ""],
    ["WEB STACK", "", "", ""],
    ["Next.js 15", "INITIALIZING", "App Router + Shadcn/UI", "In Progress"],
    ["Tailwind CSS", "INITIALIZING", "Mobile-First Design", "In Progress"],
    ["Travel Theme", "PLANNING", "Premium Documented Theme", "Next Step"],
    ["Sitejet Builder", "DECOMMISSIONED", "Replaced by Next.js", "Done"],
]

body = {"values": audit_data}
result = sheets.spreadsheets().values().update(
    spreadsheetId=sheet_id,
    range="Audit!A1",
    valueInputOption="RAW",
    body=body,
).execute()
print(f"Brain Updated: {result.get('updatedCells')} cells written to Audit sheet")
