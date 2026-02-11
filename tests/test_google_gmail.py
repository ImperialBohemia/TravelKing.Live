import sys
from unittest.mock import MagicMock

# Mock missing external dependencies
if 'google' not in sys.modules:
    sys.modules['google'] = MagicMock()
    sys.modules['google.genai'] = MagicMock()

# Ensure we are using the real core.google.gmail module, even if other tests mocked it
if 'core.google.gmail' in sys.modules:
    del sys.modules['core.google.gmail']

import pytest
from unittest.mock import patch
from core.google.gmail import GmailClient

@pytest.fixture
def gmail_client_smtp():
    return GmailClient(app_password="fake_password", email="test@example.com")

@pytest.fixture
def gmail_client_api():
    return GmailClient(access_token="fake_token", email="test@example.com")

@pytest.fixture
def gmail_client_both():
    return GmailClient(access_token="fake_token", app_password="fake_password", email="test@example.com")

def test_send_smtp_success(gmail_client_smtp):
    with patch("smtplib.SMTP_SSL") as mock_smtp:
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server

        result = gmail_client_smtp.send(to="recipient@example.com", subject="Test", body_html="<h1>Hi</h1>")

        assert result["success"] is True
        assert result["method"] == "smtp"
        mock_server.login.assert_called_with("test@example.com", "fake_password")
        mock_server.send_message.assert_called()

def test_send_api_success(gmail_client_api):
    with patch("requests.post") as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "12345"}
        mock_post.return_value = mock_response

        result = gmail_client_api.send(to="recipient@example.com", subject="Test", body_html="<h1>Hi</h1>")

        assert result["success"] is True
        assert result["method"] == "api"
        assert result["message_id"] == "12345"
        mock_post.assert_called_once()

def test_send_fallback_to_api_on_smtp_failure(gmail_client_both):
    """
    Test that if SMTP fails, it falls back to API when token is available.
    """
    with patch("smtplib.SMTP_SSL") as mock_smtp, patch("requests.post") as mock_post:
        # Mock SMTP failure
        mock_smtp.side_effect = Exception("SMTP Error")

        # Mock API success
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "api_id"}
        mock_post.return_value = mock_response

        result = gmail_client_both.send(to="recipient@example.com", subject="Test", body_html="<h1>Hi</h1>")

        assert result["success"] is True
        assert result["method"] == "api"
        assert result["message_id"] == "api_id"
        mock_post.assert_called_once()

def test_send_all_fail(gmail_client_both):
    """
    Test that if both SMTP and API fail, it returns an appropriate error.
    """
    with patch("smtplib.SMTP_SSL") as mock_smtp, patch("requests.post") as mock_post:
        # Mock SMTP failure
        mock_smtp.side_effect = Exception("SMTP Error")

        # Mock API failure
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"error": "unauthorized"}
        mock_post.return_value = mock_response

        result = gmail_client_both.send(to="recipient@example.com", subject="Test", body_html="<h1>Hi</h1>")

        assert result["success"] is False
        # If SMTP fails and falls back to API, and API fails, the method should be 'api'
        assert result["method"] == "api"
        assert result["error"] == {"error": "unauthorized"}
