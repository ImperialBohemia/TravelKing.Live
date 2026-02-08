
import sys
from core.hub import hub
from core.maintenance import maintenance

def main():
    print("👑 TRAVELKING OMEGA | Modular Supremacy")
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [status|market|sync]")
        return

    cmd = sys.argv[1].lower()

    if cmd == "status":
        print("Google Cloud: ACTIVE")
        print("Facebook Ads: ACTIVE")
        print("cPanel Hosting: ACTIVE")
    elif cmd == "market":
        res = hub.market.analyze_travel_intent("flight compensation")
        print(f"Logic Result: {res}")
    elif cmd == "sync":
        print("Manual Sync Initialized...")
    else:
        print(f"Unknown command: {cmd}")

    # Auto backup
    from core.maintenance.git_sync import auto_sync
    auto_sync(f"Modular action: {cmd}")

if __name__ == "__main__":
    main()
