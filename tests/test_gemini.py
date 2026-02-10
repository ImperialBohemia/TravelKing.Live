
import sys
from unittest.mock import MagicMock

# Mock google.genai for collection in environments without the library
if 'google' not in sys.modules:
    sys.modules['google'] = MagicMock()
    sys.modules['google.genai'] = MagicMock()

import pytest
from core.google.gemini import GeminiClient

def test_gemini_init_no_creds():
    client = GeminiClient()
    assert client.client is None
    res = client.generate_content("test")
    assert "Error" in res

def test_gemini_init_with_key():
    client = GeminiClient(api_key="test_key")
    # Even with dummy key, it shouldn't crash during init
    assert client is not None
