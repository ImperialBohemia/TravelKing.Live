
import subprocess
import time
import os

def auto_sync(action_name):
    # Dynamically resolve the project root relative to this file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(os.path.join(current_dir, "..", ".."))
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
    except:
        return False
    return False
