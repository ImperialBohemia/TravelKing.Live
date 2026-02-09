
import json
import os
from loguru import logger

class MoneyTree:
    """Enterprise Revenue Logic Centre. The definitive 'How to make money' guide."""
    
    def __init__(self):
        self.strategies = {
            "b2b": {
                "name": "Service Arbitrage (High Ticket)",
                "action": "Sell SEO/Web Dev audits to B2B leads.",
                "payout": "Stripe / Direct Bank Transfer",
                "registration_url": "https://dashboard.stripe.com/register",
                "avg_value": "$500 - $2000"
            },
            "b2c": {
                "name": "Google Affiliate Flow",
                "action": "Promote Google Cloud/Workspace via Affiliate ports.",
                "payout": "Impact / CJ / PartnerStack",
                "registration_url": "https://cloud.google.com/partners/affiliate",
                "avg_value": "$50 - $200 per day"
            },
            "video": {
                "name": "YouTube Shorts Fund / Ads",
                "action": "Monetize viral traffic via YouTube Partner Program.",
                "payout": "Google AdSense",
                "registration_url": "https://www.google.com/adsense/start/",
                "avg_value": "$100 - $1000 per month"
            },
            "passive": {
                "name": "Google Marketplace / Sheets",
                "action": "Monetize viral tools and Add-ons.",
                "payout": "Google Merchant Center",
                "registration_url": "https://merchants.google.com/",
                "avg_value": "$1 - $50 per sale"
            }
        }
        self.ledger_path = "data/finance/revenue.json"
        
    def get_strategy(self, context="hybrid"):
        """Returns the optimal money-making strategy based on input context."""
        if "lead" in context:
            return self.strategies["b2b"]
        elif "viral" in context or "traffic" in context:
            return self.strategies["b2c"]
        else:
            return self.strategies # Return Full Portfolio
            
    def record_payout(self, source, amount):
        """Tracks imaginary (simulated) or real revenue."""
        logger.success(f"💰 KA-CHING! Recorded ${amount} from {source}")
        
        ledger = {"total": 0, "transactions": []}
        if os.path.exists(self.ledger_path):
            try:
                with open(self.ledger_path, "r") as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        ledger = data
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        ledger["total"] = ledger.get("total", 0) + amount
        if "transactions" not in ledger:
            ledger["transactions"] = []
        ledger["transactions"].append({"source": source, "amount": amount})
        
        os.makedirs(os.path.dirname(self.ledger_path), exist_ok=True)
        with open(self.ledger_path, "w") as f:
            json.dump(ledger, f, indent=4)
            
        return ledger["total"]

if __name__ == "__main__":
    mt = MoneyTree()
    print(mt.get_strategy("lead"))
