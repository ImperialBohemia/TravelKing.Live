import pytest
import json
import os
from unittest.mock import MagicMock, patch, PropertyMock
import sys

# Mock modules to avoid import errors if dependencies are missing in env
mock_modules = [
    'core.connectors.google',
    'core.google.sheets',
    'core.google.gmail',
    'core.travelpayouts.flights',
    'core.utils.notifications',
    'google.oauth2',
    'googleapiclient.discovery',
    'google'
]
for mod_name in mock_modules:
    sys.modules[mod_name] = MagicMock()

# Now import the bot
from modules.concierge_bot import ConciergeBot

class TestConciergePersistence:

    @pytest.fixture(autouse=True)
    def setup_files(self, tmp_path):
        self.tmp_dir = tmp_path
        self.vault_path = tmp_path / "vault.json"
        self.state_path = tmp_path / "concierge_state.json"

        # Create vault
        vault_data = {
            "travelking": {"sheet_id": "test_sheet"},
            "google": {"app_password": "pw", "account_email": "e"},
            "travelpayouts": {"token": "t", "marker": "m"}
        }
        self.vault_path.write_text(json.dumps(vault_data))

        # Mock dependencies
        self.mock_sheets = MagicMock()
        self.mock_gmail = MagicMock()
        self.mock_flights = MagicMock()

    def test_full_flow(self):
        """Test loading state, filtering leads, processing, and saving state."""

        # 1. Setup initial state
        initial_emails = ["processed@example.com"]
        self.state_path.write_text(json.dumps(initial_emails))

        # 2. Setup leads data
        # Row 1: Already processed
        # Row 2: New
        # Row 3: New
        leads_data = [
            ["Email", "Name", "Destination"], # Header
            ["processed@example.com", "Old", "Paris"],
            ["new1@example.com", "New1", "London"],
            ["new2@example.com", "New2", "Tokyo"]
        ]

        self.mock_sheets.read_range.return_value = leads_data

        # Mock successful send
        self.mock_gmail.send.return_value = {'success': True}
        self.mock_flights.get_deals_with_links.return_value = [{'price': 100}]

        # Patch class attribute STATE_FILE and properties
        with patch.object(ConciergeBot, 'STATE_FILE', str(self.state_path)),              patch.object(ConciergeBot, 'sheets', new_callable=PropertyMock, return_value=self.mock_sheets),              patch.object(ConciergeBot, 'gmail', new_callable=PropertyMock, return_value=self.mock_gmail),              patch.object(ConciergeBot, 'flights', new_callable=PropertyMock, return_value=self.mock_flights),              patch.object(ConciergeBot, 'google_connector', new_callable=PropertyMock),              patch.object(ConciergeBot, 'notifier', new_callable=PropertyMock):

            # Init bot
            bot = ConciergeBot(vault_path=str(self.vault_path))

            # Verify loaded state
            assert "processed@example.com" in bot.processed_emails

            # Run bot
            bot.run(max_leads=10)

            # Verify processing
            # Should process new1 and new2
            # Should NOT process processed@example.com

            assert self.mock_gmail.send.call_count == 2

            # Verify state saved
            final_content = json.loads(self.state_path.read_text())
            assert "new1@example.com" in final_content
            assert "new2@example.com" in final_content
            assert "processed@example.com" in final_content

    def test_failure_handling(self):
        """Test that failed leads are NOT saved to state."""
        self.state_path.write_text(json.dumps([]))

        leads_data = [
            ["Email", "Name", "Destination"],
            ["fail@example.com", "Fail", "Nowhere"]
        ]
        self.mock_sheets.read_range.return_value = leads_data

        # Mock failed send
        self.mock_gmail.send.return_value = {'success': False, 'error': 'Simulated failure'}
        self.mock_flights.get_deals_with_links.return_value = [{'price': 100}]

        with patch.object(ConciergeBot, 'STATE_FILE', str(self.state_path)),              patch.object(ConciergeBot, 'sheets', new_callable=PropertyMock, return_value=self.mock_sheets),              patch.object(ConciergeBot, 'gmail', new_callable=PropertyMock, return_value=self.mock_gmail),              patch.object(ConciergeBot, 'flights', new_callable=PropertyMock, return_value=self.mock_flights),              patch.object(ConciergeBot, 'google_connector', new_callable=PropertyMock),              patch.object(ConciergeBot, 'notifier', new_callable=PropertyMock):

            bot = ConciergeBot(vault_path=str(self.vault_path))
            bot.run()

            # Verify logic
            assert self.mock_gmail.send.call_count == 1

            # Verify state NOT saved (or saved without the failed email)
            final_content = json.loads(self.state_path.read_text())
            assert "fail@example.com" not in final_content
