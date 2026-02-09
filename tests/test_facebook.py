import sys
from unittest.mock import MagicMock, patch

# Ensure 'requests' is in sys.modules so that FacebookConnector can be imported
# even if the library is not installed in the environment.
if 'requests' not in sys.modules:
    sys.modules['requests'] = MagicMock()

import pytest
from core.connectors.facebook import FacebookConnector

@pytest.fixture
def mock_requests():
    """Provides a mock for the 'requests' module used inside FacebookConnector."""
    # We patch the 'requests' module in core.base.connector because that is where
    # the actual API call is made in the BaseConnector.call method.
    mock = MagicMock()
    with patch('core.base.connector.requests', mock):
        yield mock

@pytest.fixture
def facebook_module():
    """Provides a FacebookConnector instance for testing."""
    vault = {
        'facebook': {
            'page_token_topstroje': 'page_token_123',
            'access_token': 'user_token_456'
        }
    }
    return FacebookConnector(vault)

def test_call_default(facebook_module, mock_requests):
    """Test FacebookConnector.call with default parameters."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"success": True}
    mock_requests.request.return_value = mock_response

    result = facebook_module.api_call("me")

    mock_requests.request.assert_called_once_with(
        "GET",
        "https://graph.facebook.com/v21.0/me",
        params={"access_token": "page_token_123"}
    )
    assert result == {"success": True}

def test_call_user_token(facebook_module, mock_requests):
    """Test FacebookConnector.call with use_page_token=False."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"success": True}
    mock_requests.request.return_value = mock_response

    result = facebook_module.api_call("me", use_page_token=False)

    mock_requests.request.assert_called_once_with(
        "GET",
        "https://graph.facebook.com/v21.0/me",
        params={"access_token": "user_token_456"}
    )
    assert result == {"success": True}

def test_call_post_method(facebook_module, mock_requests):
    """Test FacebookConnector.call with POST method."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": "123"}
    mock_requests.request.return_value = mock_response

    result = facebook_module.api_call("me/feed", method="POST", params={"message": "hello"})

    mock_requests.request.assert_called_once_with(
        "POST",
        "https://graph.facebook.com/v21.0/me/feed",
        params={"message": "hello", "access_token": "page_token_123"}
    )
    assert result == {"id": "123"}

def test_call_with_extra_params(facebook_module, mock_requests):
    """Test FacebookConnector.call with additional parameters."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": []}
    mock_requests.request.return_value = mock_response

    result = facebook_module.api_call("me/accounts", params={"fields": "name,access_token"})

    mock_requests.request.assert_called_once_with(
        "GET",
        "https://graph.facebook.com/v21.0/me/accounts",
        params={"fields": "name,access_token", "access_token": "page_token_123"}
    )
    assert result == {"data": []}
