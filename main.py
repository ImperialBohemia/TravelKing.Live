
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
    elif cmd == "intel":
        from core.intelligence import intel
        print("Synchronizing Max Logic (Google + Bing)...")
        report = intel.sync_all()
        print(f"Report Generated: {len(report['market_logic'])} data stacks active.")
    elif cmd == "scan":
        res = engine.get_live_intelligence()
        print(f"Intelligence Report: Found {len(res)} high-intent targets.")
    elif cmd == "deploy":
        print("Deployment sequence initialized...")
        # engine.deploy_authority_content(...)
    elif cmd == "sniper":
        from core.sniper import sniper
        targets = sniper.scan_for_chaos()
        for t in targets:
            pkg = sniper.generate_deployment_package(t)
            print(f"
🎯 TARGET FOUND: {t['event']}")
            print(f"🔗 SITEJET URL: {pkg['sitejet_url']}")
            print(f"📝 HEADLINE: {pkg['headline']}")
            print(f"🖼️ IMAGE PROMPT: {pkg['nano_banana_prompt']}")
            print(f"🛠️ SCHEMA: {json.dumps(pkg['schema_json'])}")
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
