
import sys
import json
from core.hub import hub

def main():
    print("👑 TRAVELKING OMEGA | Enterprise Supremacy")
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [status|market|deploy|sync]")
        return

    cmd = sys.argv[1].lower()

    if cmd == "status":
        stats = hub.status_check()
        for service, status in stats.items():
            print(f"{service}: {status}")
            
    elif cmd == "market":
        flight_id = sys.argv[2] if len(sys.argv) > 2 else "LH1160"
        res = hub.market.analyze_flight_opportunity(flight_id)
        print(f"Market Intel: {json.dumps(res, indent=4)}")
        
    elif cmd == "deploy":
        filename = sys.argv[2] if len(sys.argv) > 2 else "test_page.html"
        res = hub.deployer.deploy_sniper_page("<html>Test</html>", filename)
        print(f"Deployment: {json.dumps(res, indent=4)}")

    elif cmd == "sync":
        print("Manual Sync Initialized...")
        from core.maintenance.git_sync import auto_sync
        auto_sync("Manual User Sync")
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
