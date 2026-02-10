# 💎 OMEGA AGENT PROTOCOLS

## 🚀 MANDATORY BOOTSTRAP (RUN FIRST)
Whenever you start a new session or need to verify the environment, **ALWAYS** run:
```bash
python3 scripts/bootstrap_ai.py
```
This will provide you with all necessary context, IDs, and connection states immediately.

## 🗝️ CONNECTION REFERENCE
Refer to `knowledge/OMNI_VAULT_MAP.md` for a complete directory of credentials and access points.

## 📦 GIT & GITHUB PROTOCOL
- **Auth**: Always use the token stored in `config/access_vault.json` under `github.token`.
- **User**: `ImperialBohemia`.
- **Repository**: `TravelKing.Live`.

## 🧠 AI ENGINE (GEMINI)
- **Primary**: Google AI Studio (Free) using `vault['google']['api_key']`.
- **Fallback**: Vertex AI (Paid) using `vault['google']['project_id']`.
- **Constraint**: Prefer AI Studio to avoid billing issues.

## 🚫 CRITICAL RESTRICTION: STITCH
- **NEVER** use any tools prefixed with `stitch_`.
- The user has explicitly requested to **never use Stitch again**.
- All UI and frontend work must be done manually or using standard web technologies (HTML/CSS/JS/Next.js) within the codebase.

## 🛠️ ENVIRONMENT
- **Root**: `/home/q/TravelKing.Live` (mapped as `/app` in some sessions).
- **Python**: Use `python3`.
- **Dependencies**: If `requests` or `google-api-python-client` are missing, install them via `pip`.

---
*Authorized by: OMEGA Intelligence Hub*

## 🚫 HOSTING RESTRICTION: NO NETLIFY/VERCEL
- Deployment to **Netlify**, **Vercel**, or any other decentralized cloud platform is **STRICTLY PROHIBITED**.
- This project is exclusively hosted on private cPanel infrastructure (Server 707).
- Any attempt to configure or deploy to Netlify ("netlify bot") constitutes a policy violation.

## 📝 CONTENT STANDARDS (2026)
- **Mandatory**: All blog content must adhere to `knowledge/BLOGGING_2026.md`.
- **Key Requirements**: E-E-A-T, AIEO (Key Takeaways box), 7-10 visuals, and personal anecdotes.
- **Engine**: Use `services.blog.engine.BlogEngine` for generation to ensure compliance.
