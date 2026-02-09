import sys
import os
import unittest
from loguru import logger

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.google.factory import GoogleServiceFactory
from core.google.sheets import SheetsClient
from core.google.gmail import GmailClient
from core.google.drive import DriveClient
from core.google.indexing import IndexingClient

class TestGoogleMaxArchitecture(unittest.TestCase):
    """
    Verification Suite for Google-Max Enterprise Architecture.
    Tests factory initialization and module compliance.
    """
    def setUp(self):
        self.factory = GoogleServiceFactory()

    def test_factory_initialization(self):
        logger.info("🧪 Testing Service Factory...")
        self.assertIsNotNone(self.factory.vault)
        self.assertEqual(self.factory.project_id, "1009428807876")

    def test_sheets_client_alignment(self):
        logger.info("🧪 Testing Sheets Client...")
        client = SheetsClient(self.factory)
        self.assertIsNotNone(client.service)
        self.assertTrue(hasattr(client, 'read_range'))

    def test_gmail_client_alignment(self):
        logger.info("🧪 Testing Gmail Client...")
        client = GmailClient(self.factory)
        self.assertIsNotNone(client.service)
        self.assertTrue(hasattr(client, 'send'))

    def test_drive_client_alignment(self):
        logger.info("🧪 Testing Drive Client...")
        client = DriveClient(self.factory)
        self.assertIsNotNone(client.service)
        self.assertTrue(hasattr(client, 'upload_file'))

    def test_indexing_client_alignment(self):
        logger.info("🧪 Testing Indexing Client...")
        # Indexing API often requires specialized discovery or is build manually
        # but our factory handles standard service builds
        client = IndexingClient(self.factory.get_credentials(['https://www.googleapis.com/auth/indexing']).token)
        self.assertTrue(hasattr(client, 'submit_url'))

if __name__ == "__main__":
    unittest.main()
