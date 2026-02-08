# 🤖 AI Orchestration Guide | OMEGA Intelligence Hub

## 📌 Project Identity & Vision
**TravelKing.Live** is a specialized **Autonomous Business Engine** built for high-efficiency affiliate monetization.
- **Primary Strategy**: Project FIRE (Authority Hub). Move away from direct selling; prioritize **technical value, education, and legal authority**.
- **Domain**: `travelking.live` (Primary), `simplecode.space` (Infrastructure Provider).
- **Core Vertical**: EU261 Flight Compensation (Partnership: AirHelp).

---

## 🔌 System Connections (The Nerve System)
The system is integrated with enterprise-grade platforms. All interactions are handled via the `core.hub.hub` central orchestrator.

### ✅ Google Ecosystem (`valachman@gmail.com`) - **PERMANENT**
- **Status**: [X] ACTIVE | [X] SELF-HEALING (Auto-Refresh Enabled)
- **Vertex AI (Gemini 1.5 Pro)**: Core logic for analyzing traveler intent and generating high-authority content.
- **Google Ads (Immortal Link)**: Used for real-time keyword intelligence and market volume analysis.
- **Search Console**: Managed via API for automated indexing (currently blocked by robots/noindex).
- **Connector**: `core/connectors/google.py` (Implements `refresh()` for permanent token rotation).

### ✅ Meta/Facebook (`Stanislav Pasztorek`) - **PERMANENT**
- **Status**: [X] ACTIVE | [X] LONG-LIVED (Page Access Tokens)
- **FB Ads Manager**: Direct bridge for "Surgical Sniper" campaigns targeting specific zesto/flight disruptions.
- **Connector**: `core/connectors/facebook.py`

### ✅ Hosting & Infrastructure (`imperkhx`) - **PERMANENT**
- **Status**: [X] ACTIVE | [X] API KEY AUTH (Never Expires)
- **cPanel/WHM**: Managed on `server707.web-hosting.com`.
- **Functionality**: Programmatic creation of subdomains, file uploads, and SSL management.
- **Connector**: `core/connectors/server.py`

### ✅ Bing/Webmaster Hub - **PERMANENT**
- **Status**: [X] ACTIVE | [X] API KEY AUTH (Never Expires)
- **Bing API & IndexNow**: Automated submission of new sniper pages to Bing/IndexNow.
- **Connector**: `core/connectors/server.py` (Implements `bing_call`).

### 📦 Authentication Vault
- **Location**: `config/access_vault.json` (also linked to `/home/q/Gemini CLI/access_vault.json`).
- **Standard**: Never hardcode keys. Use `hub.vault` to retrieve credentials.

---

## ✅ Deployment & Sync - **SELF-HEALING**
- **Git Auto-Sync**: [X] ACTIVE
- **Status**: Every structural change or logic update is automatically pushed to the main repository via `core.maintenance.git_sync.auto_sync()`.
- **Logic**: Integrated into `main.py` entry point.

---

## 📂 Project Structure & Navigation (Enterprise OMEGA)
Always use relative paths from the root `/home/q/TravelKing.Live`.

| Layer | Directory | Purpose |
| :--- | :--- | :--- |
| **Base** | `core/base/` | `BaseConnector` - Unified API & Error Handling |
| **Connectors** | `core/connectors/` | Lean API wrappers (Google, FB, CPanel, Bing) |
| **Services** | `core/services/` | Business Logic Actions (`MarketIntel`, `Deployment`) |
| **Orchestrator** | `core/hub.py` | Central `OmegaHub` - Dependency Injection |
| **Knowledge** | `knowledge/` | Strategic memory (Blueprint, Styles, Intel) |
| **Interface** | `main.py` | Modular CLI Entry Point |

---

## 🛠️ Operational Standards for Jules AI
1. **The "Enterprise" Workflow**:
   - Step 1: Query `hub.market.analyze_flight_opportunity()` for disruption intelligence.
   - Step 2: Use `hub.deployer.deploy_sniper_page()` for programmatic SEO actions.
   - Step 3: All API calls MUST go through `hub.<connector>.api_call()`.
   - Step 4: Verification via `hub.status_check()`.

2. **Legal & Compliance**:
   - All pages must have `noindex, nofollow` until the 'Ready' command.
   - Content must follow HSE (UK) and EU261 technical standards to maintain "Authority" status.

3. **Zero-Storage Policy**:
   - No SQLite/MySQL for visitor data. All processing is volatile.

4. **Self-Healing**:
   - Use `core.maintenance.git_sync` to ensure all changes are tracked and backed up immediately.

---
*This guide ensures maximum alignment between Jules AI and the Project FIRE strategy.*
