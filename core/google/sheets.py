import logging
from typing import List, Dict, Any, Optional
from core.google.factory import GoogleServiceFactory
from googleapiclient.errors import HttpError
import time

class SheetsClient:
    """
    Gold Standard Google Sheets Client.
    Aligned with official v4 documentation: https://developers.google.com/sheets/api/reference/rest
    """
    def __init__(self, factory: Optional[GoogleServiceFactory] = None):
        self.factory = factory or GoogleServiceFactory()
        self.service = self.factory.get_sheets()
        self.logger = logging.getLogger("OMEGA.Sheets")

    def read_range(self, spreadsheet_id: str, range_name: str) -> List[List[str]]:
        """Official GET implementation with error handling."""
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id, range=range_name).execute()
            return result.get('values', [])
        except HttpError as error:
            self.logger.error(f"An error occurred: {error}")
            return []

    def append_row(self, spreadsheet_id: str, range_name: str, values: List[Any]) -> bool:
        """Official POST implementation for appending data."""
        try:
            body = {'values': [values]}
            self.service.spreadsheets().values().append(
                spreadsheetId=spreadsheet_id, range=range_name,
                valueInputOption="USER_ENTERED", body=body).execute()
            return True
        except HttpError as error:
            self.logger.error(f"Append failed: {error}")
            return False

    def batch_update(self, spreadsheet_id: str, requests_list: List[Dict]) -> dict:
        """Official BatchUpdate implementation for atomic operations."""
        try:
            body = {'requests': requests_list}
            return self.service.spreadsheets().batchUpdate(
                spreadsheetId=spreadsheet_id, body=body).execute()
        except HttpError as error:
            self.logger.error(f"Batch update failed: {error}")
            return {"error": str(error)}

    def get_form_responses(self, spreadsheet_id: str) -> List[Dict[str, str]]:
        """Maps spreadsheet rows to dictionaries using header row."""
        data = self.read_range(spreadsheet_id, "A:Z")
        if not data:
            return []
        headers = data[0]
        return [dict(zip(headers, row)) for row in data[1:]]
