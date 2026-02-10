import pytest
import json
from unittest.mock import MagicMock, patch, mock_open
from services.blog.engine import BlogEngine
from core.google.gemini import GeminiClient

@pytest.fixture
def mock_gemini():
    return MagicMock(spec=GeminiClient)

@pytest.fixture
def blog_engine(mock_gemini):
    return BlogEngine(mock_gemini)

def test_init(blog_engine):
    assert blog_engine.target_url == "https://villiers.ai/?id=11089"

def test_get_2026_standards_success(blog_engine):
    with patch("builtins.open", mock_open(read_data="FAKE STANDARDS CONTENT")):
        standards = blog_engine._get_2026_standards()
        assert standards == "FAKE STANDARDS CONTENT"

def test_get_2026_standards_missing(blog_engine):
    with patch("builtins.open", side_effect=FileNotFoundError):
        standards = blog_engine._get_2026_standards()
        assert "Standards: High quality" in standards

def test_create_2026_blog_post_success(blog_engine, mock_gemini):
    mock_gemini.generate_content.return_value = '{"title": "Test Blog", "seo_keywords": "test", "html_content": "<p>Content</p>"}'

    with patch.object(blog_engine, "_get_2026_standards", return_value="Standard"):
        article = blog_engine.create_2026_blog_post("Test Topic")

        assert article["title"] == "Test Blog"
        assert article["html_content"] == "<p>Content</p>"

        # Verify prompt construction
        args, _ = mock_gemini.generate_content.call_args
        prompt = args[0]
        assert "You are an elite travel journalist" in prompt
        assert "Standard" in prompt

def test_create_2026_blog_post_json_error(blog_engine, mock_gemini):
    # Simulate Gemini returning raw text instead of JSON
    mock_gemini.generate_content.return_value = "Here is your blog post: Title: Test..."

    article = blog_engine.create_2026_blog_post("Test Topic")

    # Should fallback to a safe dict
    assert "The CEO's Guide to Test Topic" in article["title"]
    assert "Here is your blog post" in article["html_content"]

def test_create_2026_blog_post_no_gemini():
    engine = BlogEngine(None)
    article = engine.create_2026_blog_post("Test")
    assert "Fallback Article" in article["title"]
    assert "AI Generation Unavailable" in article["html_content"]
