import requests
import logging
import os
from typing import List, Dict, Any, Optional

# Official SDK Imports
try:
    from googleapiclient.discovery import build
    from google.oauth2 import service_account
    GOOGLE_SDK_AVAILABLE = True
except ImportError:
    GOOGLE_SDK_AVAILABLE = False

class SheetsClient:
    """
    Gold Standard Google Sheets Client.
    Supports official SDK with Service Account and OAuth2 fallback.
    Implementation aligned with: https://developers.google.com/sheets/api/guides/concepts
    """

    BASE_URL = "https://sheets.googleapis.com/v4/spreadsheets"

    def __init__(self, token: str = None, service_account_path: str = None):
        self.token = token
        self.sa_path = service_account_path
        self.logger = logging.getLogger("OMEGA.Sheets")
        self.service = None

        if GOOGLE_SDK_AVAILABLE:
            if self.sa_path and os.path.exists(self.sa_path):
                creds = service_account.Credentials.from_service_account_file(
                    self.sa_path,
                    scopes=['https://www.googleapis.com/auth/spreadsheets']
                )
                self.service = build('sheets', 'v4', credentials=creds)
                self.logger.info("SheetsClient: Initialized with Service Account.")
            elif self.token:
                try:
                    from google.oauth2.credentials import Credentials
                    creds = Credentials(token=self.token)
                    self.service = build('sheets', 'v4', credentials=creds)
                    self.logger.info("SheetsClient: Initialized with OAuth2 Token.")
                except Exception as e:
                    self.logger.warning(f"SheetsClient: SDK Init failed, using HTTP fallback. Error: {e}")

    @property
    def headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def read_range(self, spreadsheet_id: str, range_name: str) -> List[List[str]]:
        """Reads a range using the best available method."""
        if self.service:
            try:
                result = self.service.spreadsheets().values().get(
                    spreadsheetId=spreadsheet_id, range=range_name).execute()
                return result.get('values', [])
            except Exception as e:
                self.logger.error(f"SDK Read failed: {e}")

        # HTTP Fallback
        url = f"{self.BASE_URL}/{spreadsheet_id}/values/{range_name}"
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            return res.json().get("values", [])
        return []

    def batch_update(self, spreadsheet_id: str, requests_list: List[Dict]) -> dict:
        """
        Executes multiple updates in a single atomic transaction.
        Essential for 'Gold Standard' consistency.
        """
        if self.service:
            body = {'requests': requests_list}
            return self.service.spreadsheets().batchUpdate(
                spreadsheetId=spreadsheet_id, body=body).execute()

        # HTTP Fallback
        url = f"{self.BASE_URL}/{spreadsheet_id}:batchUpdate"
        res = requests.post(url, headers=self.headers, json={'requests': requests_list})
        return res.json()

    def append_row(self, spreadsheet_id: str, range_name: str, values: List[Any]) -> bool:
        """Appends a row to the end of a sheet."""
        if self.service:
            try:
                body = {'values': [values]}
                self.service.spreadsheets().values().append(
                    spreadsheetId=spreadsheet_id, range=range_name,
                    valueInputOption="USER_ENTERED", body=body).execute()
                return True
            except Exception as e:
                self.logger.error(f"SDK Append failed: {e}")

        url = f"{self.BASE_URL}/{spreadsheet_id}/values/{range_name}:append"
        params = {"valueInputOption": "USER_ENTERED"}
        res = requests.post(url, headers=self.headers, params=params, json={"values": [values]})
        return res.status_code == 200
