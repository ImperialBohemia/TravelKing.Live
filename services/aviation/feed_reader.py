import feedparser
from loguru import logger

class VilliersFeedReader:
    """Real-time Empty Leg Fetcher from Villiers AI."""
    def __init__(self, feed_url="https://api.villiers.ai/feeds/empty-legs?id=11089"):
        self.feed_url = feed_url
        logger.info("Villiers RSS Feed Reader initialized.")

    def get_latest_deals(self):
        """Parses the RSS feed and extracts high-value flight data."""
        logger.info("📡 Fetching latest empty leg deals from Villiers...")
        feed = feedparser.parse(self.feed_url)
        
        deals = []
        for entry in feed.entries:
            # Handling custom Villiers namespace
            deal = {
                "title": entry.title,
                "link": entry.link,
                "aircraft": getattr(entry, 'villiers_aircrafttype', 'Private Jet'),
                "origin": getattr(entry, 'villiers_originairport', 'Unknown'),
                "destination": getattr(entry, 'villiers_destinationairport', 'Unknown'),
                "price": getattr(entry, 'villiers_price', 'Contact for Quote'),
                "date": getattr(entry, 'villiers_departuredate', 'Check availability'),
                "seats": getattr(entry, 'villiers_seatsavailable', 'N/A')
            }
            deals.append(deal)
        
        logger.success(f"Retrieved {len(deals)} active empty leg deals.")
        return deals
