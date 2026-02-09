import logging
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google.analytics.data_v1beta import BetaAnalyticsDataClient
import os
import json
from core.google.secrets import SecretManagerClient

class GoogleServiceFactory:
    """
    Enterprise-grade factory for Google Services.
    Follows official SDK patterns and prioritizes Google Secret Manager.
    """
    def __init__(self, vault_path='config/access_vault.json', sa_path='config/service_account.json'):
        self.vault_path = vault_path
        self.sa_path = sa_path
        self.logger = logging.getLogger("OMEGA.GoogleFactory")

        with open(self.vault_path, 'r') as f:
            self.vault = json.load(f)

        self.project_id = self.vault.get('google', {}).get('project_id', '1009428807876')
        self.sm_client = SecretManagerClient(project_id=self.project_id)

    def get_secure_key(self, key_name, local_fallback):
        """Attempts to fetch from Secret Manager, fallback to vault."""
        cloud_key = self.sm_client.get_secret(key_name)
        return cloud_key if cloud_key else local_fallback

    def get_credentials(self, scopes):
        """Standard OAuth2 Credentials with Cloud Secret integration."""
        g_vault = self.vault.get('google', {})

        # Prioritize Cloud Secrets for sensitive data
        client_secret = self.get_secure_key('GOOGLE_CLIENT_SECRET', g_vault.get('client_secret'))
        refresh_token = self.get_secure_key('GOOGLE_REFRESH_TOKEN', g_vault.get('refresh_token'))

        return Credentials(
            token=g_vault.get('access_token'),
            refresh_token=refresh_token,
            client_id=g_vault.get('client_id'),
            client_secret=client_secret,
            token_uri="https://oauth2.googleapis.com/token",
            scopes=scopes
        )

    def get_service_account_credentials(self, scopes):
        """Permanent Service Account credentials."""
        if os.path.exists(self.sa_path):
            return service_account.Credentials.from_service_account_file(
                self.sa_path, scopes=scopes)
        return None

    def build_service(self, service_name, version, scopes, use_sa=True):
        """Constructs an official discovery service object."""
        creds = None
        if use_sa:
            creds = self.get_service_account_credentials(scopes)

        if not creds:
            creds = self.get_credentials(scopes)

        return build(service_name, version, credentials=creds, cache_discovery=False)

    def get_analytics_client(self):
        scopes = ['https://www.googleapis.com/auth/analytics.readonly']
        creds = self.get_service_account_credentials(scopes) or self.get_credentials(scopes)
        return BetaAnalyticsDataClient(credentials=creds)

    def get_sheets(self):
        return self.build_service('sheets', 'v4', ['https://www.googleapis.com/auth/spreadsheets'])

    def get_gmail(self):
        return self.build_service('gmail', 'v1', ['https://www.googleapis.com/auth/gmail.send'])

    def get_drive(self):
        return self.build_service('drive', 'v3', ['https://www.googleapis.com/auth/drive'])

    def get_indexing(self):
        return self.build_service('indexing', 'v3', ['https://www.googleapis.com/auth/indexing'])
