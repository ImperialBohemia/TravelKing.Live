import os
import sys

# Add project root to path
sys.path.append(os.getcwd())

from core.connectors.travelpayouts import TravelpayoutsConnector
from core.hub import hub

def check_travelpayouts_data():
    print("\n✈️  Checking Travelpayouts Data Access...")
    
    # 1. Partner Statistics (Fields List)
    print("   -> Fetching Report Fields...")
    fields_url = "https://api.travelpayouts.com/statistics/v1/get_fields_list"
    try:
        res = hub.travelpayouts.api_call(fields_url)
        if isinstance(res, dict) and 'fields' in res:
             print(f"      ✅ Success! Found {len(res['fields'])} available fields.")
        else:
             print(f"      ❌ Failed: {res}")
    except Exception as e:
        print(f"      ❌ Exception: {e}")

    # 2. Flight Data Cache (Prices for dates)
    print("\n   -> Fetching Flight Price Cache (PRG -> LON)...")
    try:
        data = hub.travelpayouts.get_flight_disruption_data("PRG", "LON")
        if isinstance(data, list) and len(data) > 0:
            print(f"      ✅ Success! Found {len(data)} flight records.")
            print(f"      Sample: {data[0]}")
        elif isinstance(data, dict) and data.get("success") == False:
             print(f"      ❌ API Error: {data}")
        else:
             print(f"      ⚠️  No data returned or empty list: {data}")
    except Exception as e:
        print(f"      ❌ Exception: {e}")

if __name__ == "__main__":
    check_travelpayouts_data()