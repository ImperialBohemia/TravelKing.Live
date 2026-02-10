# 🌌 OMNI-VAULT MASTER MAP (v2026.MAX)

This document is the **Single Source of Truth** for AI Agents to identify and access all system connections.

## 🗝️ CORE CREDENTIAL LOCATIONS

| Service | File Path | Key Data |
| :--- | :--- | :--- |
| **Main Vault** | `config/access_vault.json` | Google, FB, Bing, TP, GitHub, Analytics, GTM |
| **Google Auth (v2)** | `data/config/google_auth_v2.json` | Client ID, Secret, Refresh Token (OAuth) |
| **Service Account** | `config/service_account.json` | Primary Google Admin Access (JSON) |
| **Token Cache** | `data/config/token_cache.json` | Last refresh timestamps and token prefixes |
| **Bluesky** | `data/config/bluesky_state.json` | Posting session and credentials |
| **cPanel** | `config/access_vault.json` (key: `cpanel`) | Host, User, API Token |

## 🚀 BOOTSTRAP PROTOCOL (For AI Agents)

1.  **Run `python3 scripts/verify_connections.py`**: Immediate check of which bridges are active.
2.  **Verify Google OAuth**: If `access_token` is expired, call `GoogleAdmin(vault).refresh_access_token()`.
3.  **Check Git/GitHub**: Access token is in `vault['github']['token']`. Use for all push/pull operations.
4.  **AI Engine**: Check `vault['google']['api_key']` for AI Studio (Free) or `project_id` for Vertex AI.

## 📦 GIT CONNECTION (HIGH DETAIL)
- **Repository**: `ImperialBohemia/TravelKing.Live`
- **Auth Method**: Personal Access Token (PAT)
- **Token Path**: `config/access_vault.json` -> `github.token`
- **User**: `ImperialBohemia`

## 📊 GOOGLE FORMS & SHEETS (HIGH DETAIL)
- **CRM Sheet ID**: `1uvNvNKei8sgmrASHE5OpQKwEANcOFjxOCdIxMWBnOQc`
- **Lead Intake**: Tab `Leads`
- **Technical Log**: Tab `Tasks`

---
*Authorized by: OMEGA Intelligence Hub*

---

## 🚫 FORBIDDEN CONNECTIONS
| Service | Status | Reason |
| :--- | :--- | :--- |
| **Stitch** | **STRICTLY FORBIDDEN** | User mandate: "no foking stitch never". DO NOT CONNECT. |
| **Netlify/Vercel** | **STRICTLY FORBIDDEN** | Mandate: "ONLY cPanel". |
