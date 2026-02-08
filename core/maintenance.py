
import subprocess
import logging
import time

class Maintenance:
    """Handles automatic synchronization with GitHub and system hygiene."""
    
    def __init__(self, root="/home/q/Gemini CLI"):
        self.root = root

    def auto_sync(self, action_name):
        """Commits and pushes all changes to GitHub automatically."""
        try:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            message = f"🤖 AUTO-SYNC: {action_name} | {timestamp}"
            
            # Git sequence
            subprocess.run(["git", "add", "."], cwd=self.root, check=True)
            # Check if there are changes to commit
            status = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=self.root)
            if status.returncode != 0:
                subprocess.run(["git", "commit", "-m", message], cwd=self.root, check=True)
                subprocess.run(["git", "push", "origin", "main"], cwd=self.root, check=True)
                logging.info(f"Maintenance: GitHub Sync Successful - {action_name}")
                return True
            else:
                logging.info("Maintenance: No changes to sync.")
                return False
        except Exception as e:
            logging.error(f"Maintenance: Git Sync Failed: {str(e)}")
            return False

maintenance = Maintenance()
