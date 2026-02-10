# TravelKing.Live — Operational Manual & Secrets

**VERSION:** 2026.1 (Sovereign Blog Pivot)
**LAST UPDATED:** 2026-02-10

## 1. Credentials (ACCESS VAULT)

**WARNING:** These are live production keys. Do not share.

**Google Cloud (Valachman)**
- **User:** valachman@gmail.com
- **Project ID:** 1009428807876
- **Services:** Indexing API, Sheets API, Drive API, Gmail API
- **App Password (Gmail):** `zzpd unbh srxl omvu`

**cPanel (Hosting)**
- **Host:** server707.web-hosting.com
- **User:** imperkhx
- **API Token:** `LUTLTTXMW901X3DUJH9FJPEM6CXNPK4D`
- **Domain:** travelking.live

**Facebook / Instagram**
- **App ID:** 696429503450342
- **Page Token (TopStroje):** `EAAJ5ZAiEqDOYBQogtaZAZAPzHmBtF8RBT4ueJQpWaImWaEN1uX6niIPO3PnStQggjvrZBqPydLSUwyGgZAcGlAqTT9drIc0ZBdgjWU3Rv0SaE5fDxx9rVIN87td1355Lex4gzJnYdXS3Ikn4tqsgcdiZBYlyPdbSLe6MctO6hifnn3ZBTZCsXxiq5h8vVzrluZCNSMmeVCDMXy2xJjKnXpyx8lfzoC`

**Travelpayouts**
- **Token:** `ae4c8d7eac860dba7ef9b0340fc4e38b`
- **Marker:** 702269

**GitHub**
- **Repo:** ImperialBohemia/TravelKing.Live
- **Token:** `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`

## 2. Architecture Overview

### Web Stack (Local -> Remote)
- **Local:** Next.js 16 + Velite + Tailwind v4 (in `web-latest/`)
- **Remote:** Static HTML/CSS/JS (in `public_html/` on server)
- **Deployment:** Python Script (`scripts/deploy_cpanel_direct.py`) connects via cPanel API and uploads `web-latest/out`.

### Content Workflow (Zero Code)
1.  **Create Post:** Add a `.md` file to `web-latest/content/posts/`
2.  **Build:** Run `cd web-latest && npx velite build && npx next build`
3.  **Deploy:** Run `./venv/bin/python3 scripts/deploy_cpanel_direct.py`

## 3. Deployment Protocol

If the website looks "old" or "broken", force a fresh deploy:

```bash
# 1. Kill any stuck processes
pkill -f "deploy_cpanel_direct"

# 2. Re-build locally
cd /home/q/TravelKing.Live/web-latest
npm run build 

# 3. Push to Server
cd /home/q/TravelKing.Live
./venv/bin/python3 scripts/deploy_cpanel_direct.py
```

## 4. Monetization & Analytics
- **Script:** `emrldtp.cc` (Hardcoded in `layout.tsx`)
- **GA4:** `G-CENSTCTLCW`
- **GTM:** `GTM-WB69V297`
