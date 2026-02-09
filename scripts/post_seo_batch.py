import sys
import os

# Add paths to sys.path
sys.path.append('/home/q/Bsky.App')

from bluesky_client import BlueskyClient
from atproto_client.utils import TextBuilder

def post_batch_to_bsky():
    client = BlueskyClient(config_path='/home/q/Bsky.App/config.json')
    client.login()
    
    posts = [
        {
            "text": "🧬 Biohacking the Skies: 2026 Jet Lag Cures. ✈️\n\nVIPs are moving beyond comfort. Light therapy, personalized hydration, and molecular diagnostics are now standard protocols for zero-fatigue journeys.\n\n#Biohacking #LuxuryAviation #EliteTravel #Wellness2026",
            "image": "/home/q/TravelKing.Live/assets/biohacking.png"
        },
        {
            "text": "📖 The Rise of 'Canon Country' Tourism. 🗺️\n\nTravel as a literary pursuit. High-intent travelers seek 'Regenerative Depth' by visiting settings of classic literature—from misty lochs to rolling hills. Simplicity meets elite culture.\n\n#CanonCountry #BespokeTravel #LiteraryTourism",
            "image": "/home/q/TravelKing.Live/assets/canon_country.png"
        },
        {
            "text": "🧠 Vibe Coding is Here: AI Search by Atmosphere. 💎\n\nSearch by 'price' is dead. Elite travelers now search by 'Vibe'—Misty, Melancholic, or Epic. AI builds itineraries based on emotional intent.\n\n#VibeCoding #AIPlan #FutureTravel #SEO2026",
            "image": "/home/q/TravelKing.Live/assets/green_aviation_tech_2026_1770641557477.png"
        }
    ]
    
    for post in posts:
        tb = TextBuilder()
        tb.text(post["text"])
        print(f"Publishing SEO Post: {post['text'][:30]}...")
        client.post_with_image(tb.build_text(), post["image"], "2026 Luxury Travel Insight", facets=tb.build_facets())
        import time
        time.sleep(5) # Brief pause between batch posts

if __name__ == "__main__":
    post_batch_to_bsky()
