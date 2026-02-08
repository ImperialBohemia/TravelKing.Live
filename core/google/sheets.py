"""
OMEGA Sheets Client
Official Docs: https://developers.google.com/sheets/api/reference/rest
Scope: https://www.googleapis.com/auth/spreadsheets

Enterprise-grade Sheets API wrapper for reading form data and writing deals.
"""

import requests
from typing import List, Dict, Any


class SheetsClient:
    """Read/Write Google Sheets via API."""
    
    BASE_URL = "https://sheets.googleapis.com/v4/spreadsheets"
    
    def __init__(self, access_token: str):
        self.token = access_token
        self.headers = {"Authorization": f"Bearer {self.token}"}
    
    def read_range(self, spreadsheet_id: str, range_name: str) -> List[List[str]]:
        """
        Read a range of cells from a spreadsheet.
        
        Args:
            spreadsheet_id: The ID from the sheet URL
            range_name: A1 notation like 'Sheet1!A1:D10'
            
        Returns:
            List of rows, each row is a list of cell values
        """
        url = f"{self.BASE_URL}/{spreadsheet_id}/values/{range_name}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json().get("values", [])
        return []
    
    def append_row(self, spreadsheet_id: str, range_name: str, values: List[Any]) -> bool:
        """
        Append a row to a spreadsheet.
        
        Args:
            spreadsheet_id: The ID from the sheet URL
            range_name: Target range like 'Sheet1!A:D'
            values: List of values for the new row
            
        Returns:
            bool: Success status
        """
        url = f"{self.BASE_URL}/{spreadsheet_id}/values/{range_name}:append"
        params = {"valueInputOption": "USER_ENTERED"}
        body = {"values": [values]}
        
        response = requests.post(url, headers=self.headers, params=params, json=body)
        return response.status_code == 200
    
    def write_range(self, spreadsheet_id: str, range_name: str, values: List[List[Any]]) -> bool:
        """
        Write data to a specific range.
        
        Args:
            spreadsheet_id: The ID from the sheet URL
            range_name: Target range like 'Sheet1!A1:D10'
            values: 2D list of values
            
        Returns:
            bool: Success status
        """
        url = f"{self.BASE_URL}/{spreadsheet_id}/values/{range_name}"
        params = {"valueInputOption": "USER_ENTERED"}
        body = {"values": values}
        
        response = requests.put(url, headers=self.headers, params=params, json=body)
        return response.status_code == 200
    
    def get_form_responses(self, spreadsheet_id: str, skip_header: bool = True) -> List[Dict[str, str]]:
        """
        Get form responses as list of dicts (assumes row 1 is header).
        
        Args:
            spreadsheet_id: Linked response sheet ID
            skip_header: Whether to skip first row
            
        Returns:
            List of response dictionaries
        """
        data = self.read_range(spreadsheet_id, "A:Z")
        if not data:
            return []
        
        headers = data[0] if data else []
        responses = []
        
        for row in data[1:] if skip_header else data:
            response_dict = {}
            for i, header in enumerate(headers):
                response_dict[header] = row[i] if i < len(row) else ""
            responses.append(response_dict)
        
        return responses
