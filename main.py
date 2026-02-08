
import sys
import os
from core.engine import engine
from core.connector import bridge

def main():
    print("👑 TRAVELKING OMEGA | System Online")
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [audit|scan|deploy]")
        return

    cmd = sys.argv[1].lower()

    if cmd == "audit":
        engine.run_full_audit()
    elif cmd == "scan":
        res = engine.get_live_intelligence()
        print(f"Intelligence Report: Found {len(res)} high-intent targets.")
    elif cmd == "deploy":
        print("Deployment sequence initialized...")
        # engine.deploy_authority_content(...)
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
