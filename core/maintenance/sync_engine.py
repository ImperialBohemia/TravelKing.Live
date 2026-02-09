"""
💎 OMEGA AUTO-SYNC & BACKUP ENGINE
Project: TravelKing.Live | Owner: Stanislav Pasztorek
Authorized by: Imperial Bohemia
Status: PERMANENT PROTOCOL ACTIVE
Description: Handles cPanel backups, GitHub Sync, and Auto-Conflict Resolution.
"""

import os
import subprocess
from datetime import datetime

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def auto_sync():
    print(f"🔄 OMEGA SYNC INITIATED: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    # 1. CPANEL BACKUP (Local Snapshot before Git)
    backup_folder = f"backups/snap_{datetime.now().strftime('%Y%m%d_%H%M')}"
    os.makedirs(backup_folder, exist_ok=True)
    run_cmd(f"cp -r core config templates index.html dashboard.py {backup_folder}/")
    print(f"   ✅ cPanel Local Snapshot Created: {backup_folder}")

    # 2. GIT PULL & MERGE (Pre-emptive)
    print("   🔍 Checking for remote updates...")
    _, err, code = run_cmd("git pull --rebase origin main")

    if code != 0:
        print(f"   ⚠️ CONFLICT DETECTED! Initiating Auto-Repair...")
        run_cmd("git rebase --abort")
        run_cmd("git pull -s recursive -X ours origin main")
        print("   ✅ Auto-Repair: Remote merged with LOCAL priority.")

    # 3. BRAIN LOGGING (Do this BEFORE commit)
    now_iso = datetime.now().isoformat()
    log_entry = f"\n- {now_iso} | SYNC PREP | Snapshot: {backup_folder}"
    with open("knowledge/TRAVELKING_KNOWLEDGE.md", "a") as f:
        f.write(log_entry)
    print("   ✅ Brain Logged.")

    # 4. GIT PUSH
    print("   🚀 Synchronizing to GitHub...")
    run_cmd("git add .")
    run_cmd(f'git commit -m "💎 OMEGA AUTO-SYNC: Permanent Snapshot {datetime.now().strftime("%Y-%m-%d %H:%M")}"')
    _, _, push_code = run_cmd("git push origin main")

    if push_code == 0:
        print("   ✅ GitHub Sync: SUCCESS")
    else:
        print("   ❌ GitHub Sync: FAILED (Check network/auth)")

if __name__ == "__main__":
    auto_sync()