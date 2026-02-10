import pytest
import json
import os
from unittest.mock import patch, mock_open, MagicMock
import sys

# Mock missing dependencies if necessary (though we installed them)
sys.modules['google.genai'] = MagicMock()
sys.modules['google.auth'] = MagicMock()

from core.hub import OmegaHub

class TestOmegaHubResilience:

    @patch('builtins.open', new_callable=mock_open, read_data='{"google": {"api_key": "valid"}}')
    def test_init_success(self, mock_file):
        """Test that OmegaHub initializes correctly with valid config."""
        # We need to patch os.path.join because the real code constructs a path
        # Actually, open() is called with a path.

        hub = OmegaHub()
        assert hub.vault['google']['api_key'] == 'valid'
        assert hub.google is not None

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_init_missing_file(self, mock_file):
        """Test that OmegaHub survives missing config file."""
        hub = OmegaHub()
        assert hub.vault == {}
        assert hub.google is not None
        # Verify it's in a safe state
        assert hub.google.token is None

    @patch('builtins.open', new_callable=mock_open, read_data='{invalid_json')
    def test_init_corrupt_json(self, mock_file):
        """Test that OmegaHub survives corrupt JSON."""
        # mock_open doesn't automatically raise JSONDecodeError on read,
        # but json.load does when fed invalid string.
        # However, mocking open returns a file object. json.load reads from it.
        # It's easier to mock json.load directly for this specific error.

        with patch('json.load', side_effect=json.JSONDecodeError("Expecting value", "doc", 0)):
            hub = OmegaHub()
            assert hub.vault == {}
            assert hub.google is not None
