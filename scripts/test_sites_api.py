import sys
import os
import json

ROOT_DIR = '/home/q/TravelKing.Live'
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from core.google.sites import SitesClient
from loguru import logger

def test_sites_access():
    # Load credentials
    vault_path = os.path.join(ROOT_DIR, 'config/access_vault.json')
    with open(vault_path, 'r') as f:
        vault = json.load(f)
    
    access_token = vault['google']['access_token']
    
    logger.info("🚀 Testing Google Sites API via Drive...")
    
    client = SitesClient(access_token)
    
    # 1. List existing sites
    logger.info("📋 Listing existing Google Sites...")
    sites = client.list_sites()
    logger.success(f"✅ Found {len(sites)} Google Sites:")
    for site in sites:
        logger.info(f"   - {site['name']} | {site.get('webViewLink', 'N/A')}")
    
    # 2. Get specific site URL
    if sites:
        site_id = sites[0]['id']
        url = client.get_site_url(site_id)
        logger.info(f"🔗 First site URL: {url}")
    
    logger.success("🎯 Google Sites API access confirmed via Drive!")

if __name__ == "__main__":
    test_sites_access()
