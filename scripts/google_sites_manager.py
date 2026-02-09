import asyncio
import json
import os
import sys

# Ensure root is in path
ROOT_DIR = '/home/q/TravelKing.Live'
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from loguru import logger

# Paths
VAULT_PATH = os.path.join(ROOT_DIR, 'config/access_vault.json')
# Use the system's chrome profile to bypass "insecure browser" blocks
USER_DATA_DIR = '/home/q/.config/google-chrome/Default'
SITE_URL = "https://sites.google.com/d/1Kc8GEiGzgo2YdyzDViq1T8NXQpipjQwF/p/13KiP0UT99cXKiYTBgzHwioVd-IucMCie/edit"

async def build_content(page, structure):
    logger.info("🛠️ Starting content building process...")
    await page.keyboard.press("e") 
    await asyncio.sleep(2)
    logger.info("⌨️ Edit mode engaged.")

async def manage_site():
    # Load credentials
    with open(VAULT_PATH, 'r') as f:
        vault = json.load(f)
    
    email = vault['google']['account_email']
    password = vault['google']['app_password'] 
    
    logger.info(f"🚀 Starting Headless Manager (Persistent Profile) for: {email}")

    async with async_playwright() as p:
        # Launch persistent context to reuse existing sessions and look legit
        context = await p.chromium.launch_persistent_context(
            user_data_dir='/home/q/TravelKing.Live/data/browser_profile', # Using a local copy to avoid locking the main profile
            headless=True,
            viewport={'width': 1920, 'height': 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = context.pages[0] if context.pages else await context.new_page()
        await Stealth().apply_stealth_async(page)

        try:
            logger.info(f"🔗 Navigating to Google Site: {SITE_URL}")
            await page.goto(SITE_URL, wait_until="networkidle", timeout=60000)
            
            # Login check
            if "accounts.google.com" in page.url:
                logger.warning("🔑 Session expired. Attempting login via persistent profile...")
                
                await page.wait_for_selector('input[type="email"]')
                await page.fill('input[type="email"]', email)
                await page.keyboard.press("Enter")
                await page.wait_for_timeout(5000)
                
                # Try password
                pw_selectors = ['input[type="password"]', 'input[name="password"]']
                pw_found = False
                for sel in pw_selectors:
                    try:
                        await page.wait_for_selector(sel, state="visible", timeout=5000)
                        await page.fill(sel, password)
                        pw_found = True
                        break
                    except:
                        continue
                
                if pw_found:
                    await page.keyboard.press("Enter")
                    await page.wait_for_load_state("networkidle", timeout=60000)

            # Check if still blocked
            if "accounts.google.com" in page.url:
                logger.error("🛑 Still blocked by Google Login. Bot detection likely.")
                await page.screenshot(path=os.path.join(ROOT_DIR, "logs/site_login_blocked.png"))
                return

            # Editor Validation
            await page.wait_for_selector('div[aria-label="Publish"]', timeout=30000)
            logger.success("🎯 Connected to Site Editor.")
            
            # Load structure and build
            STRUCTURE_PATH = os.path.join(ROOT_DIR, 'data/site_structure.json')
            with open(STRUCTURE_PATH, 'r') as f:
                structure = json.load(structure)
            await build_content(page, structure)
            
            await page.screenshot(path=os.path.join(ROOT_DIR, "logs/site_editor_connected.png"))

        except Exception as e:
            logger.error(f"💥 ERROR: {e}")
            await page.screenshot(path=os.path.join(ROOT_DIR, "logs/site_error_report.png"))
        finally:
            await context.close()

if __name__ == "__main__":
    asyncio.run(manage_site())
