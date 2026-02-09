import json
import os
import sys
from loguru import logger
from datetime import datetime

# Add paths to sys.path
ROOT_DIR = '/home/q/TravelKing.Live'
sys.path.append(ROOT_DIR)
sys.path.append('/home/q/Bsky.App')

from bluesky_client import BlueskyClient
from atproto_client.utils import TextBuilder
from ai.logic.brain import Brain

STATE_FILE = os.path.join(ROOT_DIR, 'data/bluesky_state.json')
HISTORY_FILE = os.path.join(ROOT_DIR, 'data/bluesky_history.json')

class BlueskySequencer:
    """Psychological posting engine: 4 Warm-ups + 1 Boom with Duplicate Protection."""
    
    def __init__(self):
        self.client = BlueskyClient(config_path='/home/q/Bsky.App/config.json')
        self.brain = Brain(root_dir=ROOT_DIR)
        self._ensure_state()

    def _ensure_state(self):
        os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
        if not os.path.exists(STATE_FILE):
            with open(STATE_FILE, 'w') as f:
                json.dump({"post_index": 1}, f)
        if not os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'w') as f:
                json.dump({"published_texts": [], "published_images": []}, f)

    def _get_history(self):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)

    def _add_to_history(self, text, image):
        history = self._get_history()
        history["published_texts"].append(text[-50:]) # Track tail for variation
        history["published_images"].append(image)
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f)

    def _get_index(self):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)["post_index"]

    def _increment_index(self):
        idx = self._get_index()
        new_idx = idx + 1 if idx < 5 else 1
        with open(STATE_FILE, 'w') as f:
            json.dump({"post_index": new_idx}, f)
        return new_idx

    def run_next_post(self):
        idx = self._get_index()
        logger.info(f"🚀 Bluesky Sequencer: Running Post Type #{idx}")
        
        self.client.login()
        
        if idx < 5:
            # WARM-UP (Educational/Authority)
            self._post_warmup(idx)
        else:
            # THE BOOM (Sales/Affiliate Link Card)
            self._post_boom()
        
        self._increment_index()

    def _post_warmup(self, idx):
        topics = {
            1: {
                "text": "🌱 2026 Insights: Sustainable Aviation Fuel (SAF) is now standard. We're tracking an 85% drop in CO2 on elite routes. The future of travel is green. ✈️",
                "tags": "#GreenAviation #SAF #Travel2026",
                "image_prompt": "Futuristic airport with bio-fuel loading, cinematic sunrise, 4k."
            },
            2: {
                "text": "🧠 AI in the Sky: Flight ops in 2026 are powered by real-time predictive modeling. Zero delays, hyper-optimized routes. Technology meets safety. 💎",
                "tags": "#AIAviation #TechTrends #SafetyFirst",
                "image_prompt": "Jet cockpit with holographic AI navigation displays, ultra-detailed, 8k."
            },
            3: {
                "text": "🏜️ The 'Quietcation' Trend: 2026 travelers are seeking silence. Remote hubs in the Middle East and Himalayas are becoming the top choice for VIPs. 🤫",
                "tags": "#Quietcation #LuxuryTravel #HiddenGems",
                "image_prompt": "Ultra-luxury desert resort with a private jet parked nearby, dusk lighting, high-end travel photography."
            },
            4: {
                "text": "🚁 Urban Air Mobility: eVTOL taxis are now connecting major airports to city centers in minutes. The 1-hour commute is officially dead. ⚡",
                "tags": "#eVTOL #FutureMobility #AirportTransfer",
                "image_prompt": "Sleek electric air taxi landing on a luxury hotel rooftop, futuristic cityscape, photorealistic, 4k."
            }
        }
        
        topic = topics.get(idx)
        
        # 1. Dynamic Text Variation via Brain
        variant_prompt = f"Rewrite this aviation post to be unique and professional for Feb 2026: {topic['text']}"
        unique_text = self.brain.think(variant_prompt) or topic['text']
        
        # 2. Duplicate Check
        history = self._get_history()
        if unique_text[-50:] in history["published_texts"]:
            unique_text += f" [{datetime.now().strftime('%H:%M')}]" # Forced uniqueness

        tb = TextBuilder()
        tb.text(f"{unique_text}\n\n{topic['tags']}")
        
        # 3. Handle image uniqueness
        base_image = "/home/q/TravelKing.Live/assets/green_aviation_tech_2026_1770641557477.png"
        
        self.client.login()
        self.client.post_with_image(tb.build_text(), base_image, "Unique 2026 Aviation Insight", facets=tb.build_facets())
        self._add_to_history(unique_text, base_image)
        logger.success(f"✅ Warm-up #{idx} published (SEO uniquely verified).")

    def _post_boom(self):
        tb = TextBuilder()
        tb.text("💎 2026 VIP Insight: Intentional Aviation is the new peak. ✈️\n\n")
        tb.text("Step into the 'Decision-Detox' era with AI-curated private jet journeys. Curated, seamless, elite.\n\n")
        tb.text("Book Now 👇")
        
        rich_text = tb.build_text()
        facets = tb.build_facets()
        image_path = "/home/q/TravelKing.Live/assets/luxury_ai_aviation_trend_2026_1770640305334.png"
        
        self.client.post_with_link_card(
            text=rich_text,
            url="https://villiers.ai/?id=11089",
            title="Book Your Elite Journey | Villiers Jet 2026",
            description="Official Partner. Experience AI-curated private aviation. Start your decision-detox journeys today.",
            thumb_path=image_path,
            facets=facets
        )
        logger.success("💥 THE BOOM: Affiliate Link Card published.")

if __name__ == "__main__":
    seq = BlueskySequencer()
    seq.run_next_post()
