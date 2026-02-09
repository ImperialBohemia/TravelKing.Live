import sys
import os

# Add paths to sys.path
sys.path.append('/home/q/Bsky.App')

from bluesky_client import BlueskyClient
from atproto_client.utils import TextBuilder

def post_authority_to_bsky():
    client = BlueskyClient(config_path='/home/q/Bsky.App/config.json')
    client.login()
    
    # Authority/SEO Content (No Links)
    tb = TextBuilder()
    tb.text("🌱 The Aviation Revolution: Beyond the Jet Engine. ✈️\n\n")
    tb.text("In 2026, Sustainable Aviation Fuel (SAF) is the new baseline. We're seeing an 85% reduction in carbon emissions across elite private routes.\n\n")
    tb.text("The shift to 'Green Charters' is here. 💎\n\n")
    tb.text("#GreenAviation #SAF2026 #SustainableTravel #TravelKing")
    
    rich_text = tb.build_text()
    facets = tb.build_facets()
    
    image_path = "/home/q/.gemini/antigravity/brain/e5440fd9-29de-4a08-b77d-358f4614ee8f/green_aviation_tech_2026_1770641557477.png"
    alt_text = "Futuristic aviation lounge with holographic displays showing green energy statistics."
    
    print("Publishing Authority/SEO Post to Bluesky...")
    response = client.post_with_image(rich_text, image_path, alt_text, facets=facets)
    print(f"Post published successfully! Uri: {response.uri}")

if __name__ == "__main__":
    post_authority_to_bsky()
