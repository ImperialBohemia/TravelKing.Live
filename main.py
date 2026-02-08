import sys
import os
import json
from core.engine import engine
from core.connector import bridge
from core.maintenance import maintenance

def main():
    print("👑 TRAVELKING OMEGA | System Online")
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [audit|intel|scan|deploy|sniper]")
        return

    cmd = sys.argv[1].lower()
    success = False

    try:
        if cmd == "audit":
            engine.run_full_audit()
            success = True
        elif cmd == "intel":
            from core.intelligence import intel
            print("Synchronizing Max Logic (Google + Bing)...")
            report = intel.sync_all()
            print(f"Report Generated: {len(report['market_logic'])} data stacks active.")
            success = True
        elif cmd == "scan":
            res = engine.get_live_intelligence()
            print(f"Intelligence Report: Found {len(res)} high-intent targets.")
            success = True
        elif cmd == "deploy":
            print("Deployment sequence initialized...")
            # engine.deploy_authority_content(...)
            success = True
        elif cmd == "sniper":
            from core.sniper import sniper
            targets = sniper.scan_for_chaos()
            for t in targets:
                pkg = sniper.generate_deployment_package(t)
                print(f"\n🎯 TARGET FOUND: {t['event']}")
                print(f"🔗 SITEJET URL: {pkg['sitejet_url']}")
                print(f"📝 HEADLINE: {pkg['headline']}")
                print(f"🖼️ IMAGE PROMPT: {pkg['nano_banana_prompt']}")
                print(f"🛠️ SCHEMA: {json.dumps(pkg['schema_json'])}")
            success = True
        else:
            print(f"Unknown command: {cmd}")
    except Exception as e:
        print(f"❌ Execution Error: {str(e)}")

    # FULL AUTO SYNC TO GITHUB & BRAIN
    if success:
        print("\n🔄 Performing automatic sync to GitHub & Brain Knowledge...")
        maintenance.auto_sync(f"Executed command '{cmd}'")

if __name__ == "__main__":
    main()