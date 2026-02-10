import pytest
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
