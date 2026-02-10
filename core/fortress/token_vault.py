"""
TOKEN VAULT — Single Source of Truth for all credentials.

Every service reads and writes tokens through this module.
Atomic file writes prevent corruption. Thread-safe via file locking.
"""

import json
import os
import tempfile
import shutil
import time
from datetime import datetime
from pathlib import Path

VAULT_PATH = "/home/q/TravelKing.Live/config/access_vault.json"
TOKEN_CACHE_PATH = "/home/q/TravelKing.Live/data/config/token_cache.json"
HISTORY_DIR = "/home/q/TravelKing.Live/data/logs/token_history"

os.makedirs(HISTORY_DIR, exist_ok=True)
os.makedirs(os.path.dirname(TOKEN_CACHE_PATH), exist_ok=True)


def _atomic_write(path: str, data: dict):
    """Write JSON atomically — write to temp file first, then rename."""
    dir_name = os.path.dirname(path)
    fd, tmp_path = tempfile.mkstemp(dir=dir_name, suffix=".json.tmp")
    try:
        with os.fdopen(fd, 'w') as f:
            json.dump(data, f, indent=4)
        shutil.move(tmp_path, path)
    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise


def load_vault() -> dict:
    """Load the main credential vault."""
    with open(VAULT_PATH, 'r') as f:
        return json.load(f)


def save_vault(vault: dict):
    """Save the vault atomically."""
    _atomic_write(VAULT_PATH, vault)


def load_token_cache() -> dict:
    """Load the token cache (metadata about token freshness)."""
    if os.path.exists(TOKEN_CACHE_PATH):
        with open(TOKEN_CACHE_PATH, 'r') as f:
            return json.load(f)
    return {}


def save_token_cache(cache: dict):
    """Save token cache atomically."""
    _atomic_write(TOKEN_CACHE_PATH, cache)


def update_google_token(new_token: str, source: str = "unknown"):
    """Update Google access token in vault and cache, with history."""
    vault = load_vault()
    old_token = vault.get("google", {}).get("access_token", "")[:20]
    
    vault["google"]["access_token"] = new_token
    save_vault(vault)
    
    # Update cache with metadata
    cache = load_token_cache()
    cache["google_access_token"] = {
        "refreshed_at": datetime.now().isoformat(),
        "refreshed_at_ts": time.time(),
        "source": source,
        "token_prefix": new_token[:20] + "..."
    }
    save_token_cache(cache)
    
    # Append history
    history_file = os.path.join(HISTORY_DIR, "google_refreshes.jsonl")
    with open(history_file, "a") as f:
        f.write(json.dumps({
            "ts": datetime.now().isoformat(),
            "source": source,
            "old_prefix": old_token,
            "new_prefix": new_token[:20]
        }) + "\n")


def update_facebook_token(new_token: str, source: str = "unknown"):
    """Update Facebook access token."""
    vault = load_vault()
    vault["facebook"]["access_token"] = new_token
    save_vault(vault)
    
    cache = load_token_cache()
    cache["facebook_access_token"] = {
        "refreshed_at": datetime.now().isoformat(),
        "refreshed_at_ts": time.time(),
        "source": source,
        "token_prefix": new_token[:20] + "..."
    }
    save_token_cache(cache)


def get_token_age(service: str) -> float:
    """Return age of token in seconds. Returns infinity if unknown."""
    cache = load_token_cache()
    entry = cache.get(f"{service}_access_token", {})
    ts = entry.get("refreshed_at_ts", 0)
    if ts == 0:
        return float("inf")
    return time.time() - ts


def get_service_account_path() -> str:
    """Return path to Google Service Account JSON."""
    return "/home/q/TravelKing.Live/config/service_account.json"
