import unittest
from unittest.mock import MagicMock, patch, PropertyMock
import os
import json
import sys

# Mock missing dependencies before importing the bot
mock_modules = [
    'core.connectors.google',
    'core.google.sheets',
    'core.google.gmail',
    'core.travelpayouts.flights',
    'core.utils.notifications',
    'google.oauth2',
    'googleapiclient.discovery',
    'google',
    'google.genai'
]
for mod_name in mock_modules:
    sys.modules[mod_name] = MagicMock()

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestConciergeBot(unittest.TestCase):
    def setUp(self):
        self.vault_data = {
            "travelking": {"sheet_id": "test_sheet_id"},
            "google": {"app_password": "test_pw", "account_email": "test@gmail.com"},
            "travelpayouts": {"token": "test_token", "marker": "test_marker"}
        }
        with open('test_vault.json', 'w') as f:
            json.dump(self.vault_data, f)

        # Mock service account path
        self.sa_path = 'test_sa.json'
        with open(self.sa_path, 'w') as f:
            json.dump({"test": "data"}, f)

    def tearDown(self):
        if os.path.exists('test_vault.json'):
            os.remove('test_vault.json')
        if os.path.exists('test_sa.json'):
            os.remove('test_sa.json')

    def test_process_lead_dynamic_origin(self):
        # We need to import ConciergeBot inside the test method because we mocked modules
        from modules.concierge_bot import ConciergeBot

        # Patching properties to avoid actual initialization
        with patch.object(ConciergeBot, 'google_connector', new_callable=PropertyMock), \
             patch.object(ConciergeBot, 'sheets', new_callable=PropertyMock), \
             patch.object(ConciergeBot, 'gmail', new_callable=PropertyMock), \
             patch.object(ConciergeBot, 'flights', new_callable=PropertyMock), \
             patch.object(ConciergeBot, 'notifier', new_callable=PropertyMock):

            bot = ConciergeBot(vault_path='test_vault.json', sa_path='test_sa.json')

            # Mock search_flights to see how it's called
            bot.search_flights = MagicMock(return_value=[{'price': 100, 'airline': 'Test Air', 'link': 'http', 'departure_at': '2026-01-01'}])

            # Mock gmail property to return a mock gmail client
            mock_gmail_client = MagicMock()
            bot.gmail.return_value = mock_gmail_client
            mock_gmail_client.send.return_value = {'success': True}

            # Test case 1: Origin provided
            lead = {
                'Email': 'user@example.com',
                'Name': 'John',
                'Destination': 'London',
                'Origin': 'NYC'
            }
            bot.process_lead(lead)
            bot.search_flights.assert_called_with('NYC', 'LON')

            # Test case 2: Origin Port provided
            lead = {
                'Email': 'user2@example.com',
                'Name': 'Jane',
                'Destination': 'Paris',
                'Origin Port': 'SFO'
            }
            bot.process_lead(lead)
            bot.search_flights.assert_called_with('SFO', 'PAR')

            # Test case 3: Default fallback
            lead = {
                'Email': 'user3@example.com',
                'Name': 'Bob',
                'Destination': 'Dubai'
            }
            bot.process_lead(lead)
            bot.search_flights.assert_called_with('PRG', 'DUB')

            # Test case 4: Formatting (lowercase, whitespace)
            lead = {
                'Email': 'user4@example.com',
                'Name': 'Alice',
                'Destination': 'tokyo  ',
                'Origin': '  lax  '
            }
            bot.process_lead(lead)
            bot.search_flights.assert_called_with('LAX', 'TOK')

if __name__ == '__main__':
    unittest.main()
