"""
Visual Engine — Nano Banana Pro + Imagen 4 prompt engineering.

Models:
 - Nano Banana Pro (Gemini 3 Pro Image): Complex scenes, 4K, identity locking
 - Imagen 4: Photorealistic, text rendering specialist
 - Veo 3: VIDEO — LOCKED, requires explicit user permission

Prompt standards defined in: knowledge/visual_standards.md
"""
import logging

logger = logging.getLogger(__name__)


class VisualEngine:
    """Enterprise image generation via Google Flow models."""

    # ── SAFETY: Video generation is LOCKED ──
    VIDEO_LOCKED = True
    VIDEO_CREDITS_PER_VIDEO = 100
    VIDEO_MONTHLY_LIMIT = 1000

    def __init__(self):
        self.style_guide = (
            "Hyper-realistic 4K photography, Phase One 100MP, "
            "Cinematic lighting, Luxury aesthetic"
        )
        logger.info("Visual Engine initialized (Images: UNLIMITED, Video: LOCKED)")

    # ──────────────────────────────────────
    # NANO BANANA PRO — Complex Scenes
    # ──────────────────────────────────────
    def prompt_luxury_scene(self, subject: str, setting: str,
                            action: str = "standing elegantly") -> dict:
        """
        Generate a world-class prompt for Nano Banana Pro.
        Structure: Subject + Action + Setting + Style + Technicals
        """
        prompt = (
            f"A high-fidelity photo of {subject}, {action}, {setting}. "
            f"Style: {self.style_guide}. "
            f"Lighting: Golden hour with dramatic rim light. "
            f"Camera: 85mm lens, f/1.8, razor-sharp focus on subject, "
            f"beautiful bokeh background. "
            f"Color: Professional color grading, rich textures, "
            f"deep blacks and vibrant gold accents."
        )
        logger.info(f"Prompt crafted: {subject[:30]}...")
        return {
            "prompt": prompt,
            "model": "Nano Banana Pro (Gemini 3 Pro Image)",
            "resolution": "4K",
            "usage": "Unlimited",
        }

    def prompt_travel_destination(self, destination: str,
                                   mood: str = "luxurious and serene") -> dict:
        """Specialized prompt for travel destination hero images."""
        prompt = (
            f"Breathtaking aerial panorama of {destination}. "
            f"Mood: {mood}. Shot from a private helicopter at golden hour. "
            f"Ultra-wide 16mm lens, dramatic clouds parting to reveal "
            f"crystal-clear waters and pristine architecture below. "
            f"National Geographic quality, 8K resolution, "
            f"vivid but natural color palette."
        )
        return {
            "prompt": prompt,
            "model": "Nano Banana Pro",
            "resolution": "8K",
            "usage": "Unlimited",
        }

    # ──────────────────────────────────────
    # IMAGEN 4 — Text & Typography
    # ──────────────────────────────────────
    def prompt_text_asset(self, text: str, style: str = "Gold Foil",
                          background: str = "dark obsidian glass") -> dict:
        """
        Generate a prompt for Imagen 4's superior text rendering.
        Use for: logos, banners, typography graphics.
        """
        prompt = (
            f"High-resolution graphic design asset. "
            f"Large, legible text reading '{text}'. "
            f"Style: {style} typography on a {background} texture. "
            f"Reflective surfaces, sharp edges, 8K resolution, "
            f"centered composition, premium brand aesthetic."
        )
        return {
            "prompt": prompt,
            "model": "Imagen 4 (Text-Specialist)",
            "quality": "Elite",
            "usage": "Unlimited",
        }

    def prompt_branded_card(self, headline: str, subtext: str = "") -> dict:
        """Generate a prompt for a branded social media card."""
        prompt = (
            f"Professional social media card for TravelKing. "
            f"Headline in elegant sans-serif: '{headline}'. "
            f"{'Subtext: ' + repr(subtext) + '. ' if subtext else ''}"
            f"Brand colors: Midnight Blue (#0A192F) and Gold (#D4AF37). "
            f"Dark glassmorphic background with subtle gradient. "
            f"Aspect ratio 1:1, 4K, modern luxury design."
        )
        return {
            "prompt": prompt,
            "model": "Imagen 4",
            "quality": "Elite",
            "usage": "Unlimited",
        }

    # ──────────────────────────────────────
    # VEO 3 — VIDEO (LOCKED)
    # ──────────────────────────────────────
    def prompt_video(self, description: str) -> dict:
        """
        VIDEO GENERATION IS LOCKED.
        Returns prompt metadata but does NOT generate.
        Only the user can unlock this manually.
        """
        if self.VIDEO_LOCKED:
            logger.warning("VIDEO GENERATION IS LOCKED. User permission required.")
            return {
                "prompt": description,
                "model": "Veo 3",
                "status": "LOCKED — requires user permission",
                "credits_cost": self.VIDEO_CREDITS_PER_VIDEO,
            }
        # This path is never reached unless user explicitly unlocks
        return {
            "prompt": description,
            "model": "Veo 3",
            "status": "READY",
            "credits_cost": self.VIDEO_CREDITS_PER_VIDEO,
        }
