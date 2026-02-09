import logging
import os
from typing import Optional, List, Dict
from core.google.factory import GoogleServiceFactory
from core.utils.backoff import google_api_backoff
from googleapiclient.http import MediaFileUpload

class DriveClient:
    """
    Gold Standard Google Drive Client.
    Supports official SDK and resumable uploads with retries.
    """
    def __init__(self, factory: Optional[GoogleServiceFactory] = None):
        self.factory = factory or GoogleServiceFactory()
        self.service = self.factory.get_drive()
        self.logger = logging.getLogger("OMEGA.Drive")

    @google_api_backoff()
    def upload_file(self, file_path: str, name: str, mime_type: str = "application/pdf",
                    folder_id: Optional[str] = None) -> dict:
        """Official Resumable Upload implementation."""
        file_metadata = {'name': name}
        if folder_id:
            file_metadata['parents'] = [folder_id]

        media = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        self.logger.info(f"DriveClient: File uploaded. ID: {file.get('id')}")
        return {"success": True, "id": file.get('id')}

    @google_api_backoff()
    def make_public(self, file_id: str) -> str:
        """Official Permissions API implementation."""
        permission = {'role': 'reader', 'type': 'anyone'}
        self.service.permissions().create(fileId=file_id, body=permission).execute()
        return f"https://drive.google.com/file/d/{file_id}/view?usp=sharing"

    @google_api_backoff()
    def list_files(self, folder_id: Optional[str] = None) -> List[Dict]:
        """Official List implementation."""
        query = f"'{folder_id}' in parents" if folder_id else None
        results = self.service.files().list(
            q=query, pageSize=100, fields="nextPageToken, files(id, name, mimeType)").execute()
        return results.get('files', [])
