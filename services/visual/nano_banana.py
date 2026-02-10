import json
from loguru import logger

class NanoBananaGenerator:
    """Enterprise HQ Image Generator using Google's Nano Banana (Gemini 3 Pro)."""
    
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.style_guide = "Hyper-realistic 4K photography, Phase One 100MP, Cinematic lighting, Luxury aesthetic"
        logger.info("Nano Banana Visual Engine: ULTIMATE MODE READY (4K HQ + Reasoning).")

    def generate_luxury_visual(self, subject, setting, action="standing elegantly"):
        """
        Generates a world-class luxury prompt for Nano Banana Pro.
        Structure: Subject + Action + Setting + Style + Technicals
        """
        hq_prompt = (
            f"A high-fidelity photo of {subject}, {action}, {setting}. "
            f"Style: {self.style_guide}. "
            f"Lighting: Golden hour with dramatic rim light. "
            f"Camera: 85mm lens, f/1.8, razor-sharp focus on subject, beautiful bokeh background. "
            f"Color: Professional color grading, rich textures, deep blacks and vibrant gold accents."
        )
        
        logger.info(f"🎨 Orchestrating 4K Visual: {subject[:20]} in {setting[:20]}...")
        
        return {
            "prompt": hq_prompt,
            "model": "Nano Banana Pro (Gemini 3 Pro Image)",
            "resolution": "4K",
            "usage": "Unlimited (Free Plan)",
            "status": "Ready for Generation"
        }

    def craft_text_asset(self, text, style="Gold Foil"):
        """Specialized logic for Imagine 4's superior text rendering."""
        prompt = (
            f"High-resolution graphic design asset. Large, legible text reading '{text}'. "
            f"Style: {style} typography on a dark obsidian glass texture. "
            f"Reflective surfaces, sharp edges, 8k resolution, centered composition."
        )
        return {
            "prompt": prompt,
            "model": "Imagine 4 (Text-Specialist Mode)",
            "quality": "Elite"
        }

