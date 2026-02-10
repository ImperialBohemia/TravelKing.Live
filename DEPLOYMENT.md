# TravelKing.Live Deployment Guide

**CRITICAL:** This project relies on a REMOTE cPanel server (`server707.web-hosting.com`).
Changes made to the local `web-latest` or `public_html` directories DO NOT automatically reflect on the live site (`travelking.live`).

## Deployment Workflow

1.  **Build Local Site:**
    Generate the static site from the Next.js source.
    ```bash
    cd web-latest
    npx velite build
    npx next build --webpack
    ```
    This creates the `web-latest/out` directory.

2.  **Deploy to Remote Server:**
    Run the deployment script to upload `out/` to the remote `public_html`.
    ```bash
    # Ensure venv is active or use full path
    ./venv/bin/python3 scripts/deploy_cpanel_direct.py
    ```

## Behind the Scenes
The script `scripts/deploy_cpanel_direct.py`:
- Connects to `server707.web-hosting.com` using credentials in `config/access_vault.json`.
- Uploads the contents of `web-latest/out` to:
    - `public_html` (Main Site)
    - `TravelKing` (Backup/Subdirectory)

## Troubleshooting
- If changes are not visible, ensure you ran the deployment script.
- Check `config/access_vault.json` for correct cPanel credentials.
- Verify `web-latest/out` contains the latest build artifacts.
