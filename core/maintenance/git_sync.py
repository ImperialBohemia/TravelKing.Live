import subprocess
import time
import os

def auto_sync(action_name):
    # Find the project root relative to this file
    # core/maintenance/git_sync.py -> core/maintenance -> core -> root
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    message = f"🤖 MODULAR-SYNC: {action_name} | {timestamp}"
    
    try:
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        # Check for changes
        status = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=root)
        if status.returncode != 0:
            subprocess.run(["git", "commit", "-m", message], cwd=root, check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=root, check=True)
            return True
    except Exception as e:
        print(f"Sync error: {e}")
        return False
    return False
