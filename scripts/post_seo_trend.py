import sys
import os

# Add paths to sys.path
sys.path.append('/home/q/Bsky.App')

from bluesky_client import BlueskyClient
from atproto_client.utils import TextBuilder

def post_trend_to_bsky():
    client = BlueskyClient(config_path='/home/q/Bsky.App/config.json')
    client.login()
    
    # Max SEO Optimization (Google/Bing/FB Shortened)
    tb = TextBuilder()
    tb.text("💎 2026 VIP Insight: Intentional Aviation. ✈️\n\n")
    tb.text("Elite travelers are moving to 'Decision-Detox' journeys via AI Private Jet Concierges for high-fidelity, curated itineraries. Seamless & Luxurious.\n\n")
    tb.text("Book Now 👇\n\n")
    tb.text("#PrivateJet2026 #LuxuryAviation #AIConcierge #SEO")
    
    rich_text = tb.build_text()
    facets = tb.build_facets()
    
    image_path = "/home/q/.gemini/antigravity/brain/e5440fd9-29de-4a08-b77d-358f4614ee8f/luxury_ai_aviation_trend_2026_1770640305334.png"
    
    print("Publishing Max-SEO Trend Post (Link Card) to Bluesky...")
    response = client.post_with_link_card(
        text=rich_text, 
        url="https://villiers.ai/?id=11089",
        title="Private Jet Charter 2026 | Exclusive AI Itineraries",
        description="Official Villiers Jet Partner. Secure your intentional travel experience with AI-curated private aviation. Decision-detox starts here. 💎",
        thumb_path=image_path,
        facets=facets
    )
    print(f"Post published successfully! Uri: {response.uri}")

if __name__ == "__main__":
    post_trend_to_bsky()
