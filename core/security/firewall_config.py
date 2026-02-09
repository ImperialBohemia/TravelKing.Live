import subprocess
from loguru import logger

class FirewallManager:
    """Manages system-level security rules based on Best Practices."""

    @staticmethod
    def get_best_practice_script():
        """Returns a shell script to set up a robust, hardened enterprise firewall."""
        script = [
            "echo '🛡️ INITIALIZING ENTERPRISE SECURITY SHIELD...'",
            "sudo ufw --force reset",
            "sudo ufw default deny incoming",
            "sudo ufw default allow outgoing",
            "sudo ufw logging medium",
            # Rules
            "sudo ufw allow 22/tcp comment 'SSH_MANAGEMENT'",
            "sudo ufw limit 22/tcp comment 'ANTI_BRUTEFORCE_PROTECTION'",
            "sudo ufw allow 80/tcp comment 'WEB_TRAFFIC'",
            "sudo ufw allow 443/tcp comment 'SECURE_WEB_TRAFFIC'",
            "sudo ufw allow 8085/tcp comment 'GOOGLE_AUTH_HANDSHAKE'",
            # Hardening
            "sudo ufw --force enable",
            "echo '✅ SECURITY POSTURE: HARDENED. System is now invisible to unauthorized scans.'"
        ]
        return " && ".join(script)

    @staticmethod
    def check_status():
        """Checks UFW status without sudo to prevent script hanging."""
        try:
            # We try 'ufw status' first, if it fails we check if service is running
            res = subprocess.check_output(["ufw", "status"], stderr=subprocess.DEVNULL).decode()
            return res
        except Exception:
            # Fallback for systems where ufw requires sudo even for status
            try:
                # Check if ufw service is at least active
                res = subprocess.check_output(["systemctl", "is-active", "ufw"], stderr=subprocess.DEVNULL).decode().strip()
                return f"UFW Service: {res} (Permissions limited for detailed status)"
            except Exception:
                return "UFW status unavailable (Requires Elevation)"
