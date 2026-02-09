
import os
import re
from rich.console import Console
from rich.panel import Panel

console = Console()

def scan_for_secrets(directory):
    patterns = {
        "Google API Key": r"AIza[0-9A-Za-z-_]{35}",
        "Facebook Access Token": r"EAACEdEose0cBA[0-9A-Za-z]+",
        "Generic Secret": r"(?i)api_key|api_token|secret_key|password"
    }
    
    findings = []
    for root, dirs, files in os.walk(directory):
        if ".git" in root or "venv" in root or ".nvm" in root:
            continue
        for file in files:
            if file.endswith((".py", ".json", ".env", ".sh", ".html")):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", errors="ignore") as f:
                        content = f.read()
                        for name, pattern in patterns.items():
                            if re.search(pattern, content):
                                findings.append(f"{name} found in {path}")
                except:
                    pass
    return findings

if __name__ == "__main__":
    console.print(Panel("🔒 [bold red]Antigravity Enterprise Security Shield[/bold red]", border_style="red"))
    console.print("Scanning for exposed secrets...")
    
    # Check the vault
    vault = "/home/q/TravelKing.Live/config/access_vault.json"
    if os.path.exists(vault):
        st = os.stat(vault)
        if st.st_mode & 0o077:
            console.print(f"⚠️  [yellow]CRITICAL:[/yellow] {vault} has loose permissions ({oct(st.st_mode)[-3:]}). Fixing to 600...")
            os.chmod(vault, 0o600)
        else:
            console.print(f"✅ Vault permissions verified (600).")
    
    findings = scan_for_secrets("/home/q/TravelKing.Live")
    if findings:
        for f in findings:
            console.print(f"🔍 {f}")
    else:
        console.print("✅ No plaintext secrets found in sensitive files.")
