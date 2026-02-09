import urllib.parse

def generate_looker_link():
    print("💎 OMEGA DASHBOARD GENERATOR")

    # Base Looker Studio Template URL (Standard Google Marketing Template)
    # We use a constructed URL to guide the user to create a report with specific connectors.

    base_url = "https://lookerstudio.google.com/reporting/create?"

    params = {
        "c.reportId": "marketing-ecommerce", # Suggesting a marketing template
        "ds.connector": "google_sheets",     # Primary connector suggestion
        "ds.type": "sheet",
        "ds.spreadsheetId": "1uvNvNKei8sgmrASHE5OpQKwEANcOFjxOCdIxMWBnOQc", # Your TravelKing Sheet
    }

    # Since we can't programmatically "create" the Looker report via API without complex provisioning,
    # we generate a "Magic Link" that sets up the context.

    # Actually, the best way is to instruct the user to connect the two data sources we prepared.

    print("\n📊 DATA SOURCES READY FOR LOOKER STUDIO:")
    print("1. Google Sheets (CRM Data):")
    print("   - Leads count, Status (Won/Lost), Value (€)")
    print("2. Google Analytics 4 (Traffic Data):")
    print("   - Visits, Clicks, CTR, Source (Organic/Bing)")

    print("\n🚀 ACTION PLAN:")
    print("I cannot 'push' a report to your Looker account (permissions).")
    print("But I have prepared the DATA PIPES.")
    print("\nGo to Looker Studio -> Create -> Data Source -> Google Sheets -> Select 'TravelKing'")

if __name__ == "__main__":
    generate_looker_link()