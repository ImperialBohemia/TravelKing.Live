import os
import shutil
from loguru import logger


class Janitor:
    """Manages system hygiene and log rotation."""

    def __init__(self, root="/home/q/TravelKing.Live"):
        self.root = root

    def clean(self):
        """Removes temporary build artifacts (Optimized)."""
        targets = ["__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache"]
        skip_dirs = ["0", ".venv", "venv", ".git", "node_modules"]
        
        for r, dirs, _ in os.walk(self.root):
            # Prune directories to skip scanning them
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            for d in dirs:
                if d in targets:
                    target_path = os.path.join(r, d)
                    try:
                        shutil.rmtree(target_path)
                    except Exception as e:
                        logger.warning(f"Failed to remove {target_path}: {e}")
        return "🧹 System cleaned and optimized."

    def rotate(self, log_path="data/logs/main.log"):
        """Ensures logs stay within limits."""
        full_path = os.path.join(self.root, log_path)
        if os.path.exists(full_path) and os.path.getsize(full_path) > 10 * 1024 * 1024:
            shutil.move(full_path, full_path + ".old")
            return "Logs rotated."
        return "Log size nominal."

    def lint(self):
        """Runs enterprise-grade linting using Ruff."""
        import subprocess

        try:
            res = subprocess.run(
                ["./venv/bin/ruff", "check", self.root], capture_output=True, text=True
            )
            if res.returncode == 0:
                return "Linting: Perfect. No issues found."
            return f"Linting: Anomalies detected.\n{res.stdout}"
        except Exception as e:
            return f"Linting: Failed to execute: {e}"
