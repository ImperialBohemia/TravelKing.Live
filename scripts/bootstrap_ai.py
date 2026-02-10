import json
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

def bootstrap():
    print("🚀 OMEGA AI BOOTSTRAP: INITIALIZING SYSTEM STATE...")
    print("-" * 50)

    vault_path = os.path.join(ROOT_DIR, "config/access_vault.json")
    if not os.path.exists(vault_path):
        print("❌ CRITICAL: Vault missing at " + vault_path)
        return

    with open(vault_path, 'r') as f:
        vault = json.load(f)

    # 1. Identity
    print("\n[IDENTITY]")
    print(f"Project  : TravelKing OMEGA")
    print(f"Owner    : Stanislav Pasztorek")
    print(f"GitHub   : {vault.get('github', {}).get('user', 'ImperialBohemia')}")

    # 2. Key Bridges
    print("\n[BRIDGES]")
    services = ['google', 'facebook', 'cpanel', 'bing', 'travelpayouts', 'github']
    for s in services:
        status = "✅ CONFIGURED" if s in vault else "⚪ MISSING"
        print(f"{s:15}: {status}")

    # 3. Google Specifics
    print("\n[GOOGLE CONFIG]")
    g = vault.get('google', {})
    print(f"Email    : {g.get('account_email') or g.get('email')}")
    print(f"Project  : {g.get('project_id')}")
    print(f"AI Key   : {'✅ PRESENT' if g.get('api_key') else '⚪ MISSING (Using Vertex Fallback)'}")

    # 4. Sheet IDs
    print("\n[RESOURCES]")
    tk = vault.get('travelking', {})
    print(f"CRM Sheet: {tk.get('sheet_id')}")
    print(f"GA4 ID   : {vault.get('analytics', {}).get('measurement_id')}")

    print("\n" + "-" * 50)
    print("✅ BOOTSTRAP COMPLETE: Agent is now fully context-aware.")

if __name__ == "__main__":
    bootstrap()
