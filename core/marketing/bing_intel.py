
import requests
import json
from core.hub import hub

def check_bing_keywords():
    print("💎 BING INTELLIGENCE: Keyword Data Check...")

    # 1. Get Verified Sites
    # We already know the key works from previous checks

    # 2. Get Query Stats (Keyword Performance)
    # Endpoint: GetQueryStats
    # This shows what users are ACTUALLY searching for to find the site

    url = "https://ssl.bing.com/webmaster/api.svc/json/GetQueryStats?apikey=" + hub.vault['bing']['api_key']
    site_url = "https://travelking.live" # or http variant

    # We need to know the site URL exactly as registered in Bing
    # Let's list sites first
    sites_url = "https://ssl.bing.com/webmaster/api.svc/json/GetUserSites?apikey=" + hub.vault['bing']['api_key']
    try:
        res = requests.get(sites_url).json()
        if 'd' in res and len(res['d']) > 0:
            site_entry = res['d'][0]
            site_url = site_entry['Url']
            print(f"✅ Verified Site: {site_url}")

            # Now get keywords for this site
            stats_url = f"https://ssl.bing.com/webmaster/api.svc/json/GetQueryStats?apikey={hub.vault['bing']['api_key']}&siteUrl={site_url}"
            stats = requests.get(stats_url).json()

            if 'd' in stats:
                print(f"📊 Keyword Data Points: {len(stats['d'])}")
                for q in stats['d'][:5]:
                    print(f"   - {q['Query']} (Impressions: {q['Impressions']})")
            else:
                print("⚠️  No keyword data yet (Site is new).")

        else:
            print("⚠️  No sites verified in Bing yet. (Auto-verification might take time)")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    check_bing_keywords()
