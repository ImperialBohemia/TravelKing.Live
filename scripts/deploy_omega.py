import os
import sys
import time
from pathlib import Path

# Add root to sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from core.connectors.cpanel import CPanelConnector

def deploy_to(cp, local_root, remote_root):
    """
    Enterprise-grade deployment to cPanel.
    Handles Next.js static exports including hidden directories.
    """
    print(f"\n🚀 OMEGA DEPLOY: {remote_root}")
    print(f"Source: {local_root}")

    local_root = Path(local_root)
    count = 0
    errors = 0

    # 1. Collect all directories and files
    all_dirs = []
    all_files = []
    for root, dirs, files in os.walk(local_root):
        rel_path = os.path.relpath(root, local_root)
        remote_parent = remote_root if rel_path == "." else f"{remote_root}/{rel_path}"

        for d in dirs:
            all_dirs.append((remote_parent, d))
        for f in files:
            all_files.append((remote_parent, f, Path(root) / f))

    # 2. Create directories (sorted by depth)
    print("📁 Synchronizing Directory Structure...")
    all_dirs.sort(key=lambda x: x[0].count('/'))
    for parent, name in all_dirs:
        try:
            res = cp.mkdir(parent, name)
            # Success or already exists is fine
        except Exception as e:
            print(f"  [WARN] MKDIR {parent}/{name}: {e}")

    # 3. Upload files
    print("📄 Synchronizing Assets...")
    for remote_dir, filename, local_file in all_files:
        ext = local_file.suffix.lower()
        # Skip heavy binaries to avoid UAPI timeouts
        if ext in ['.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.woff', '.woff2', '.ttf']:
            continue

        success = False
        for attempt in range(3):
            try:
                with open(local_file, 'r', encoding='utf-8', errors='ignore') as fh:
                    content = fh.read()

                res = cp.save_file(remote_dir, filename, content)
                if res.get("status") == 1:
                    count += 1
                    success = True
                    break
                time.sleep(1)
            except Exception as e:
                time.sleep(2)

        if not success:
            print(f"  [FAIL] {remote_dir}/{filename}")
            errors += 1

    print(f"\n✅ DEPLOY COMPLETE: {count} assets synced, {errors} errors.")

def main():
    from core.settings import load_vault
    try:
        vault = load_vault()
        cp = CPanelConnector(vault)
        if cp.test_connection().get("status") != "OK":
            print("❌ cPanel Connection Failed. Check your access_vault.json")
            return
    except Exception as e:
        print(f"❌ Initialization Error: {e}")
        return

    # Default to TravelKing static export folder
    local_king = ROOT_DIR / "TravelKing"
    if not local_king.exists():
        print(f"❌ Source directory {local_king} not found.")
        return

    deploy_to(cp, local_king, "public_html")

if __name__ == "__main__":
    main()
