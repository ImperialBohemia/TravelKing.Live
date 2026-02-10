"""
TravelKing.Live — Central Settings Module.

Single source of truth for all paths and configuration.
Every module imports from here instead of building its own paths.
"""
from pathlib import Path
import json
import os

# ══════════════════════════════════════════════
# PATHS
# ══════════════════════════════════════════════
ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT_DIR / "config"
DATA_DIR = ROOT_DIR / "data"
LOGS_DIR = ROOT_DIR / "logs"
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
TEMPLATES_DIR = ROOT_DIR / "templates"
SCRIPTS_DIR = ROOT_DIR / "scripts"

VAULT_PATH = CONFIG_DIR / "access_vault.json"
SA_PATH = CONFIG_DIR / "service_account.json"

# ══════════════════════════════════════════════
# VAULT LOADER (Lazy, cached)
# ══════════════════════════════════════════════
_vault_cache = None


def load_vault() -> dict:
    """Load the access vault from disk. Result is cached after first call."""
    global _vault_cache
    if _vault_cache is None:
        if not VAULT_PATH.exists():
            raise FileNotFoundError(f"Access vault not found at {VAULT_PATH}")
        with open(VAULT_PATH, "r") as f:
            _vault_cache = json.load(f)
    return _vault_cache


def reload_vault() -> dict:
    """Force-reload the vault (e.g. after token refresh)."""
    global _vault_cache
    _vault_cache = None
    return load_vault()


# ══════════════════════════════════════════════
# SERVICE ACCOUNT LOADER
# ══════════════════════════════════════════════
def get_sa_credentials(scopes: list):
    """
    Build Google credentials.
    Try Service Account first, fallback to OAuth2 from vault if missing.
    """
    from google.oauth2 import service_account
    from google.oauth2.credentials import Credentials

    # 1. Try Service Account
    if SA_PATH.exists():
        return service_account.Credentials.from_service_account_file(
            str(SA_PATH), scopes=scopes
        )

    # 2. Try OAuth2 Fallback from Vault
    try:
        vault = load_vault()
        g = vault.get("google", {})
        if g.get("refresh_token"):
            return Credentials(
                token=g.get("access_token"),
                refresh_token=g.get("refresh_token"),
                token_uri="https://oauth2.googleapis.com/token",
                client_id=g.get("client_id"),
                client_secret=g.get("client_secret"),
                scopes=scopes
            )
    except:
        pass

    raise FileNotFoundError(f"Neither Service Account ({SA_PATH}) nor valid OAuth2 credentials found in vault.")


# ══════════════════════════════════════════════
# CONSTANTS
# ══════════════════════════════════════════════
GOOGLE_SHEETS_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]
GOOGLE_DRIVE_SCOPES = [
    "https://www.googleapis.com/auth/drive",
]
GOOGLE_FULL_SCOPES = GOOGLE_SHEETS_SCOPES + GOOGLE_DRIVE_SCOPES + [
    "https://www.googleapis.com/auth/indexing",
]

FACEBOOK_GRAPH_API_VERSION = "v21.0"
FACEBOOK_GRAPH_BASE_URL = f"https://graph.facebook.com/{FACEBOOK_GRAPH_API_VERSION}"

TRAVELPAYOUTS_BASE_URL = "https://api.travelpayouts.com"

INDEXNOW_ENGINES = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://search.seznam.cz/indexnow",
]

# ══════════════════════════════════════════════
# LOGGING
# ══════════════════════════════════════════════
LOG_FORMAT = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} | {message}"

# Ensure log directory exists
LOGS_DIR.mkdir(parents=True, exist_ok=True)
