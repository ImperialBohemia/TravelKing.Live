import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from loguru import logger

class DriveHandler:
    """Manages the 2TB Google Drive storage as a profit asset hub."""
    
    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/drive']
        self.service = self._authenticate()

    def _authenticate(self):
        # We expect a service_account.json in data/config/
        key_path = "data/config/google_service_account.json"
        if os.path.exists(key_path):
            creds = service_account.Credentials.from_service_account_file(key_path, scopes=self.scopes)
            return build('drive', 'v3', credentials=creds)
        logger.warning("⚠️ Google Service Account not found. Drive features disabled.")
        return None

    def create_client_folder(self, client_name):
        """Creates a dedicated folder for a lead on your 2TB Drive."""
        if not self.service:
            return None
        
        file_metadata = {
            'name': f"Audit_{client_name}",
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = self.service.files().create(body=file_metadata, fields='id').execute()
        folder_id = folder.get('id')
        
        # Set public permissions (View only) for the pitch link
        self.service.permissions().create(
            fileId=folder_id,
            body={'type': 'anyone', 'role': 'viewer'}
        ).execute()
        
        logger.success(f"📂 Created secure folder for {client_name} (ID: {folder_id})")
        return folder_id

    def upload_audit(self, folder_id, file_path):
        """Uploads a PDF/Report to the client's folder."""
        if not self.service:
            return None
        
        file_metadata = {
            'name': os.path.basename(file_path),
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_path, mimetype='application/pdf')
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')
