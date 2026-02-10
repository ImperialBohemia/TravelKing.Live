"""
Google API Connector — per official google-api-python-client docs.

Handles: Sheets, Drive, Gmail SMTP, and Indexing API.
Auth: Service Account (primary), OAuth refresh (fallback).

Docs:
 - Sheets: https://developers.google.com/sheets/api/quickstart/python
 - Drive:  https://developers.google.com/drive/api/v3/reference
 - Gmail:  https://support.google.com/a/answer/176600
 - Index:  https://developers.google.com/search/apis/indexing-api/v3/using-api
"""
import json
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from core.settings import load_vault, get_sa_credentials, GOOGLE_FULL_SCOPES

logger = logging.getLogger(__name__)


class GoogleConnector:
    """Unified Google API bridge using Service Account + SMTP App Password."""

    def __init__(self, vault: dict = None):
        self.vault = vault or load_vault()
        self.google_cfg = self.vault.get("google", {})
        self.travelking_cfg = self.vault.get("travelking", {})
        self._sheets_service = None
        self._drive_service = None
        self._indexing_service = None

    # ──────────────────────────────────────
    # SERVICE BUILDERS (lazy, cached)
    # ──────────────────────────────────────
    @property
    def sheets(self):
        """Google Sheets API v4 service. Built per official quickstart."""
        if self._sheets_service is None:
            from googleapiclient.discovery import build
            creds = get_sa_credentials(GOOGLE_FULL_SCOPES)
            self._sheets_service = build("sheets", "v4", credentials=creds)
        return self._sheets_service

    @property
    def drive(self):
        """Google Drive API v3 service."""
        if self._drive_service is None:
            from googleapiclient.discovery import build
            creds = get_sa_credentials(GOOGLE_FULL_SCOPES)
            self._drive_service = build("drive", "v3", credentials=creds)
        return self._drive_service

    @property
    def indexing(self):
        """Google Indexing API v3 service."""
        if self._indexing_service is None:
            from googleapiclient.discovery import build
            creds = get_sa_credentials(GOOGLE_FULL_SCOPES)
            self._indexing_service = build("indexing", "v3", credentials=creds)
        return self._indexing_service

    # ──────────────────────────────────────
    # SHEETS OPERATIONS
    # ──────────────────────────────────────
    @property
    def sheet_id(self) -> str:
        return self.travelking_cfg.get("sheet_id", "")

    def sheets_read(self, range_str: str) -> list:
        """Read values from a sheet range. Returns list of rows."""
        result = self.sheets.spreadsheets().values().get(
            spreadsheetId=self.sheet_id, range=range_str
        ).execute()
        return result.get("values", [])

    def sheets_write(self, range_str: str, values: list) -> dict:
        """Write values to a sheet range."""
        body = {"values": values}
        return self.sheets.spreadsheets().values().update(
            spreadsheetId=self.sheet_id,
            range=range_str,
            valueInputOption="RAW",
            body=body,
        ).execute()

    def sheets_append(self, range_str: str, values: list) -> dict:
        """Append rows to a sheet."""
        body = {"values": values}
        return self.sheets.spreadsheets().values().append(
            spreadsheetId=self.sheet_id,
            range=range_str,
            valueInputOption="RAW",
            body=body,
        ).execute()

    def sheets_ensure_tab(self, tab_name: str):
        """Create a sheet tab if it doesn't exist."""
        meta = self.sheets.spreadsheets().get(
            spreadsheetId=self.sheet_id
        ).execute()
        existing = [s["properties"]["title"] for s in meta["sheets"]]
        if tab_name not in existing:
            body = {"requests": [{"addSheet": {"properties": {"title": tab_name}}}]}
            self.sheets.spreadsheets().batchUpdate(
                spreadsheetId=self.sheet_id, body=body
            ).execute()
            logger.info(f"Created sheet tab: {tab_name}")

    # ──────────────────────────────────────
    # DRIVE OPERATIONS
    # ──────────────────────────────────────
    def drive_list_files(self, query: str = None, max_results: int = 20) -> list:
        """List files in Drive. Query follows Drive API search syntax."""
        params = {"pageSize": max_results, "fields": "files(id, name, mimeType, modifiedTime)"}
        if query:
            params["q"] = query
        result = self.drive.files().list(**params).execute()
        return result.get("files", [])

    def drive_upload_text(self, name: str, content: str, folder_id: str = None) -> str:
        """Upload a text file to Drive. Returns file ID."""
        import io
        from googleapiclient.http import MediaIoBaseUpload
        metadata = {"name": name}
        if folder_id:
            metadata["parents"] = [folder_id]
        media = MediaIoBaseUpload(io.BytesIO(content.encode()), mimetype="text/plain")
        file = self.drive.files().create(
            body=metadata, media_body=media, fields="id"
        ).execute()
        return file["id"]

    # ──────────────────────────────────────
    # GMAIL SMTP (App Password)
    # ──────────────────────────────────────
    def send_email(self, to: str, subject: str, body_html: str) -> bool:
        """
        Send email via Gmail SMTP with App Password.
        Per: https://support.google.com/a/answer/176600
        """
        email = self.google_cfg.get("account_email")
        app_password = self.google_cfg.get("app_password")
        if not email or not app_password:
            logger.error("Gmail SMTP: Missing account_email or app_password in vault")
            return False

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"TravelKing <{email}>"
        msg["To"] = to
        msg.attach(MIMEText(body_html, "html"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
            server.starttls()
            server.login(email, app_password)
            server.sendmail(email, to, msg.as_string())
            server.quit()
            logger.info(f"Email sent to {to}")
            return True
        except Exception as e:
            logger.error(f"Gmail SMTP error: {e}")
            return False

    # ──────────────────────────────────────
    # INDEXING API
    # ──────────────────────────────────────
    def index_url(self, url: str, action: str = "URL_UPDATED") -> dict:
        """
        Submit URL to Google for indexing.
        Per: https://developers.google.com/search/apis/indexing-api/v3/using-api
        action: URL_UPDATED or URL_DELETED
        """
        body = {"url": url, "type": action}
        return self.indexing.urlNotifications().publish(body=body).execute()

    # ──────────────────────────────────────
    # HEALTH CHECK
    # ──────────────────────────────────────
    def test_connection(self) -> dict:
        """Test all Google services. Returns status dict."""
        results = {}

        # Sheets
        try:
            meta = self.sheets.spreadsheets().get(
                spreadsheetId=self.sheet_id
            ).execute()
            results["sheets"] = {"status": "OK", "title": meta["properties"]["title"]}
        except Exception as e:
            results["sheets"] = {"status": "FAIL", "error": str(e)[:100]}

        # Drive
        try:
            about = self.drive.about().get(fields="user").execute()
            results["drive"] = {"status": "OK", "user": about["user"]["emailAddress"]}
        except Exception as e:
            results["drive"] = {"status": "FAIL", "error": str(e)[:100]}

        # Gmail
        try:
            email = self.google_cfg.get("account_email")
            app_pw = self.google_cfg.get("app_password")
            server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
            server.starttls()
            server.login(email, app_pw)
            server.quit()
            results["gmail"] = {"status": "OK", "email": email}
        except Exception as e:
            results["gmail"] = {"status": "FAIL", "error": str(e)[:100]}

        return results
