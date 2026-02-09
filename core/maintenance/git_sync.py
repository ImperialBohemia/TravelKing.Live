import subprocess
import logging


class GitSync:
    """Handles automatic Git operations to keep the repository in sync with system state."""

    def __init__(self, root="/home/q/SimpleCodeSpace"):
        self.root = root

    def sync(self, message, push=False):
        """Adds, commits, and optionally pushes changes (Optimized)."""
        try:
            # Check for changes efficiently
            status_cmd = ["git", "status", "--porcelain"]
            status = subprocess.check_output(status_cmd, cwd=self.root, timeout=10).decode().strip()
            
            if not status:
                return False

            logging.info(f"🔄 Git Stage: {message}")
            subprocess.run(["git", "add", "."], cwd=self.root, check=True, timeout=30)
            
            import time
            fresh_msg = f"{message} | {time.strftime('%H:%M:%S')}"
            subprocess.run(["git", "commit", "-m", fresh_msg], cwd=self.root, check=True, timeout=30)

            if push:
                logging.info("🚀 Git Push requested...")
                subprocess.run(["git", "pull", "--rebase", "origin", "main"], cwd=self.root, check=True, timeout=60)
                subprocess.run(["git", "push", "origin", "main"], cwd=self.root, check=True, timeout=60)
            
            return True
        except subprocess.TimeoutExpired as e:
            logging.error(f"❌ Git Sync Timed Out: {e}")
            return False
        except Exception as e:
            logging.error(f"❌ Git Sync Failed: {e}")
            return False
