import pytest
from unittest.mock import patch
from core.engine.visual import VisualEngine

def test_prompt_travel_destination_basic():
    """Test with default mood."""
    engine = VisualEngine()
    destination = "Maldives"
    result = engine.prompt_travel_destination(destination)

    assert isinstance(result, dict)
    assert "prompt" in result
    assert "model" in result
    assert "resolution" in result
    assert "usage" in result

    assert destination in result["prompt"]
    assert "luxurious and serene" in result["prompt"]
    assert result["model"] == "Nano Banana Pro"
    assert result["resolution"] == "8K"

def test_prompt_travel_destination_custom_mood():
    """Test with a custom mood."""
    engine = VisualEngine()
    destination = "Swiss Alps"
    mood = "adventurous and chilly"
    result = engine.prompt_travel_destination(destination, mood=mood)

    assert destination in result["prompt"]
    assert mood in result["prompt"]
    assert "Breathtaking aerial panorama" in result["prompt"]

def test_prompt_travel_destination_structure():
    """Verify the exact structure of the returned dictionary."""
    engine = VisualEngine()
    result = engine.prompt_travel_destination("Anywhere")

    expected_keys = {"prompt", "model", "resolution", "usage"}
    assert set(result.keys()) == expected_keys
    assert result["usage"] == "Unlimited"

def test_prompt_luxury_scene_basic():
    """Test luxury scene with default action."""
    engine = VisualEngine()
    subject = "A billionaire"
    setting = "a private island"
    result = engine.prompt_luxury_scene(subject, setting)

    assert subject in result["prompt"]
    assert setting in result["prompt"]
    assert "standing elegantly" in result["prompt"]
    assert engine.style_guide in result["prompt"]
    assert result["model"] == "Nano Banana Pro (Gemini 3 Pro Image)"
    assert result["resolution"] == "4K"

def test_prompt_luxury_scene_custom_action():
    """Test luxury scene with a custom action."""
    engine = VisualEngine()
    subject = "A supermodel"
    setting = "a penthouse balcony"
    action = "sipping vintage champagne"
    result = engine.prompt_luxury_scene(subject, setting, action=action)

    assert subject in result["prompt"]
    assert setting in result["prompt"]
    assert action in result["prompt"]
    assert "standing elegantly" not in result["prompt"]

def test_prompt_text_asset_basic():
    """Test text asset with default style and background."""
    engine = VisualEngine()
    text = "TravelKing"
    result = engine.prompt_text_asset(text)

    assert f"'{text}'" in result["prompt"]
    assert "Gold Foil" in result["prompt"]
    assert "dark obsidian glass" in result["prompt"]
    assert result["model"] == "Imagen 4 (Text-Specialist)"
    assert result["quality"] == "Elite"

def test_prompt_text_asset_custom():
    """Test text asset with custom style and background."""
    engine = VisualEngine()
    text = "Luxury"
    style = "Silver Chrome"
    background = "white marble"
    result = engine.prompt_text_asset(text, style=style, background=background)

    assert f"'{text}'" in result["prompt"]
    assert style in result["prompt"]
    assert background in result["prompt"]

def test_prompt_branded_card_no_subtext():
    """Test branded card without subtext."""
    engine = VisualEngine()
    headline = "Exclusive Deals"
    result = engine.prompt_branded_card(headline)

    assert f"'{headline}'" in result["prompt"]
    assert "Subtext" not in result["prompt"]
    assert "TravelKing" in result["prompt"]
    assert result["model"] == "Imagen 4"

def test_prompt_branded_card_with_subtext():
    """Test branded card with subtext."""
    engine = VisualEngine()
    headline = "Limited Offer"
    subtext = "Book now and save 50%"
    result = engine.prompt_branded_card(headline, subtext=subtext)

    assert f"'{headline}'" in result["prompt"]
    assert f"'{subtext}'" in result["prompt"]
    assert "Subtext" in result["prompt"]

def test_prompt_video_locked():
    """Test video generation when locked."""
    engine = VisualEngine()
    description = "A drone shot of Paris"
    # Ensure it's locked by default
    engine.VIDEO_LOCKED = True
    result = engine.prompt_video(description)

    assert result["prompt"] == description
    assert "LOCKED" in result["status"]
    assert result["credits_cost"] == engine.VIDEO_CREDITS_PER_VIDEO

def test_prompt_video_unlocked():
    """Test video generation when unlocked."""
    engine = VisualEngine()
    description = "Sunset over Santorini"

    # Mock VIDEO_LOCKED to False
    with patch.object(VisualEngine, 'VIDEO_LOCKED', False):
        result = engine.prompt_video(description)

    assert result["prompt"] == description
    assert result["status"] == "READY"
    assert result["credits_cost"] == engine.VIDEO_CREDITS_PER_VIDEO
