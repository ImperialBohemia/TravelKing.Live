"""
Enterprise Full Audit — Live integration test for all connectors.

Runs real API calls against every service and reports results.
This is the master verification script.
"""
import sys
import os
import json
from datetime import datetime

# Ensure project root is on path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.connectors import (
    GoogleConnector, FacebookConnector, TravelpayoutsConnector,
    BingConnector, CPanelConnector,
)
from core.settings import load_vault


def run_full_audit():
    """Run live tests against all connectors and return results."""
    vault = load_vault()
    results = {}
    total = 0
    passed = 0

    connectors = [
        ("cPanel", CPanelConnector(vault)),
        ("Google (SA)", GoogleConnector(vault)),
        ("Facebook", FacebookConnector(vault)),
        ("Travelpayouts", TravelpayoutsConnector(vault)),
        ("Bing IndexNow", BingConnector(vault)),
    ]

    # Also test Gmail and GitHub separately
    print("=" * 50)
    print("  ENTERPRISE FULL AUDIT")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    for name, connector in connectors:
        total += 1
        try:
            result = connector.test_connection()
            # Google returns sub-results (sheets, drive, gmail)
            if isinstance(result, dict) and "status" not in result:
                # Multi-service result: check if all sub-services are OK
                all_ok = all(
                    v.get("status") == "OK"
                    for v in result.values()
                    if isinstance(v, dict)
                )
                status = "OK" if all_ok else "PARTIAL"
                result = {"status": status, "services": result}
            status = result.get("status", "UNKNOWN")
            ok = status == "OK"
            if ok:
                passed += 1
            icon = "OK" if ok else "FAIL"
            print(f"  [{icon}] {name:25s} | {json.dumps(result)[:80]}")
            results[name] = result
        except Exception as e:
            print(f"  [FAIL] {name:25s} | {str(e)[:80]}")
            results[name] = {"status": "ERROR", "error": str(e)[:100]}

    # GitHub (separate test)
    total += 1
    try:
        import requests
        gh = vault.get("github", {})
        r = requests.get(
            "https://api.github.com/user",
            headers={"Authorization": f"token {gh.get('token', '')}"},
            timeout=10,
        )
        if r.status_code == 200:
            passed += 1
            user = r.json().get("login", "?")
            print(f"  [OK]   {'GitHub':25s} | user={user}")
            results["GitHub"] = {"status": "OK", "user": user}
        else:
            print(f"  [FAIL] {'GitHub':25s} | HTTP {r.status_code}")
            results["GitHub"] = {"status": "FAIL", "http": r.status_code}
    except Exception as e:
        print(f"  [FAIL] {'GitHub':25s} | {str(e)[:80]}")
        results["GitHub"] = {"status": "ERROR", "error": str(e)[:100]}

    # Domain + SSL
    total += 1
    try:
        import requests
        r = requests.get("https://travelking.live", timeout=10)
        if r.status_code == 200:
            passed += 1
            print(f"  [OK]   {'Domain + SSL':25s} | HTTPS 200, {len(r.text)} bytes")
            results["Domain"] = {"status": "OK", "bytes": len(r.text)}
        else:
            print(f"  [FAIL] {'Domain + SSL':25s} | HTTP {r.status_code}")
            results["Domain"] = {"status": "FAIL", "http": r.status_code}
    except Exception as e:
        print(f"  [FAIL] {'Domain + SSL':25s} | {str(e)[:80]}")
        results["Domain"] = {"status": "ERROR", "error": str(e)[:100]}

    print()
    print(f"  SCORE: {passed}/{total} ({int(passed / total * 100) if total else 0}%)")
    print("=" * 50)

    return {"results": results, "passed": passed, "total": total}


if __name__ == "__main__":
    run_full_audit()
