import sys
import os

# Add paths to sys.path
sys.path.append('/home/q/Bsky.App')

from bluesky_client import BlueskyClient
from atproto_client.utils import TextBuilder

def post_trend_to_bsky():
    client = BlueskyClient(config_path='/home/q/Bsky.App/config.json')
    client.login()
    
    # Use TextBuilder to create a "Rich Text" post with facets (hyperlinks)
    tb = TextBuilder()
    tb.text("🚀 SEO Trend 2026: The rise of the AI Jet Concierge. 💎\n\n")
    tb.text("Private aviation is going fully autonomous with hyper-personalized AI integration. Efficiency meets peak luxury.\n\n")
    tb.text("Secure your flight: ")
    tb.link("Book Now ✈️", "https://villiers.ai/?id=11089")
    tb.text("\n\n#AIAviation #LuxuryTravel #SEO #TravelKing")
    
    rich_text = tb.build_text()
    facets = tb.build_facets()
    
    image_path = "/home/q/.gemini/antigravity/brain/e5440fd9-29de-4a08-b77d-358f4614ee8f/luxury_ai_aviation_trend_2026_1770640305334.png"
    alt_text = "Luxury aviation lounge with a holographic AI itinerary display during sunset."
    
    print("Publishing SEO Trend Post (with Hyperlink) to Bluesky...")
    response = client.post_with_image(rich_text, image_path, alt_text, facets=facets)
    print(f"Post published successfully! Uri: {response.uri}")

if __name__ == "__main__":
    post_trend_to_bsky()
