import os
import sys
import logging
import time
from datetime import datetime

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.hub import hub

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/sniper_bot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('SniperBot')

class SniperBot:
    """
    Autonomous Sniper Bot:
    Monitors delays -> Generates Pages -> Deploys -> Indexes.
    """
    def __init__(self):
        self.hub = hub
        logger.info("🎯 OMEGA Sniper Bot initialized.")

    def run_cycle(self):
        """One execution cycle of the sniper loop."""
        logger.info("🔍 Sniper Cycle: Searching for new targets...")

        targets = self.hub.sniper.find_high_intent_targets()

        for target in targets:
            flight_id = target['flight_number']
            logger.info(f"🎯 Target Found: {flight_id}")

            # 1. Prepare Data
            strike_data = self.hub.sniper.prepare_sniper_data(target)

            # 2. Generate HTML (Mocking template injection)
            filename = f"delay-{flight_id.lower()}.html"
            html_content = f"<html><body><h1>Flight {flight_id} Delayed!</h1><p>Claim your {strike_data['CLAIM_AMOUNT']} now.</p></body></html>"

            # 3. Deploy & Index
            result = self.hub.deployer.deploy_sniper_page(html_content, filename)

            logger.info(f"✅ Sniper Strike Success: {result['url']}")

    def run_forever(self, interval=3600):
        """Runs the sniper bot on a schedule."""
        logger.info(f"🚀 Sniper Bot engaged. Heartbeat every {interval}s.")
        while True:
            try:
                self.run_cycle()
            except Exception as e:
                logger.error(f"⚠️ Sniper Cycle Error: {e}")

            time.sleep(interval)

if __name__ == "__main__":
    bot = SniperBot()
    bot.run_cycle()
