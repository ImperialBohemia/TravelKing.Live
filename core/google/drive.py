"""
OMEGA Drive Client
Official Docs: https://developers.google.com/drive/api/reference/rest/v3
Scope: https://www.googleapis.com/auth/drive

Enterprise-grade Drive API wrapper for PDF uploads and public asset management.
"""

import requests
from typing import Optional


class DriveClient:
    """Manage files on Google Drive via API."""

    BASE_URL = "https://www.googleapis.com/drive/v3"
    UPLOAD_URL = "https://www.googleapis.com/upload/drive/v3/files"

    def __init__(self, access_token: str):
        self.token = access_token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def upload_file(self, file_path: str, name: str, mime_type: str = "application/pdf",
                    folder_id: Optional[str] = None) -> dict:
        """
        Upload a file to Google Drive.

        Args:
            file_path: Local path to file
            name: Name for the file in Drive
            mime_type: MIME type of the file
            folder_id: Optional folder ID to upload into

        Returns:
            dict: File metadata including ID
        """
        metadata = {"name": name}
        if folder_id:
            metadata["parents"] = [folder_id]

        # Resumable upload for reliability
        headers = {
            **self.headers,
            "Content-Type": "application/json"
        }

        init_response = requests.post(
            f"{self.UPLOAD_URL}?uploadType=resumable",
            headers=headers,
            json=metadata
        )

        if init_response.status_code != 200:
            return {"success": False, "error": init_response.json()}

        upload_url = init_response.headers.get("Location")

        with open(file_path, "rb") as f:
            file_data = f.read()

        upload_response = requests.put(
            upload_url,
            headers={"Content-Type": mime_type},
            data=file_data
        )

        if upload_response.status_code == 200:
            return {"success": True, **upload_response.json()}
        return {"success": False, "error": upload_response.json()}

    def make_public(self, file_id: str) -> str:
        """
        Make a file publicly accessible and return the share link.

        Args:
            file_id: The Drive file ID

        Returns:
            str: Public share URL
        """
        permissions_url = f"{self.BASE_URL}/files/{file_id}/permissions"
        permission = {"role": "reader", "type": "anyone"}

        requests.post(permissions_url, headers=self.headers, json=permission)

        return f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"

    def list_files(self, folder_id: Optional[str] = None, limit: int = 100) -> list:
        """
        List files in Drive or a specific folder.

        Args:
            folder_id: Optional folder to list
            limit: Max files to return

        Returns:
            list: List of file metadata dicts
        """
        url = f"{self.BASE_URL}/files"
        params = {"pageSize": limit, "fields": "files(id,name,mimeType,webViewLink)"}

        if folder_id:
            params["q"] = f"'{folder_id}' in parents"

        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json().get("files", [])
        return []
