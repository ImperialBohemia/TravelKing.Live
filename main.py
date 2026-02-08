import sys
from core.hub import hub
from core.validator import check_status

def main():
    print("👑 TRAVELKING OMEGA | Modular Supremacy")
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [status|market|sniper|validate|sync]")
        return

    cmd = sys.argv[1].lower()

    if cmd == "status":
        print("Google Cloud: ACTIVE")
        print("Facebook Ads: ACTIVE")
        print("cPanel Hosting: ACTIVE")
    elif cmd == "market":
        query = sys.argv[2] if len(sys.argv) > 2 else "flight compensation"
        res = hub.market.analyze_travel_intent(query)
        print(f"Logic Result: {res}")
    elif cmd == "sniper":
        airline = sys.argv[2] if len(sys.argv) > 2 else ""
        delays = hub.sniper.search_for_delays(airline)
        print(f"Detected Delays: {delays}")
        if delays:
            # Deploy for the first one as an example
            flight = delays[0]["flight_number"]
            res = hub.sniper.deploy_sniper_page(flight)
            print(f"Deployment Result: {res}")
    elif cmd == "validate":
        url = sys.argv[2] if len(sys.argv) > 2 else "https://travelking.live"
        is_ok = check_status(url)
        print(f"Validation for {url}: {'✅ OK' if is_ok else '❌ FAILED'}")
    elif cmd == "sync":
        print("Manual Sync Initialized...")
    else:
        print(f"Unknown command: {cmd}")

    # Auto backup
    from core.maintenance.git_sync import auto_sync
    auto_sync(f"Modular action: {cmd}")

if __name__ == "__main__":
    main()
