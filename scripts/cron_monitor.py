#!/home/q/TravelKing.Live/venv/bin/python3
"""
CRON WRAPPER FOR GUARDIAN PROTOCOL
Executed every 1 minute by System Cron.
"""
import sys
import os
import time
from datetime import datetime

# Force root path
ROOT_DIR = "/home/q/TravelKing.Live"
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from loguru import logger

# Configure Logger for automated runs
log_file = os.path.join(ROOT_DIR, "data/logs/cron_monitor.log")
logger.add(log_file, rotation="10 MB", retention="10 days", level="INFO")

def run_job():
    logger.info(f"⏰ Cron Execution Started: {datetime.now()}")
    try:
        from core.maintenance.guardian import Guardian
        g = Guardian(root_dir=ROOT_DIR)
        
        # Run health check + Google Sheet update
        results = g.perform_health_check()
        
        # Check for critical failures for local alert
        failures = [s for s, d in results['services'].items() if d['status'] == 'FAILED']
        if failures:
            logger.error(f"❌ CRITICAL FAILURES DETECTED: {failures}")
        else:
            logger.info("✅ System Healthy")
            
    except Exception as e:
        logger.exception(f"🔥 CRON FATAL ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_job()
