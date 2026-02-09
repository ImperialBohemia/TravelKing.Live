import asyncio
import os
import sys

ROOT_DIR = '/home/q/TravelKing.Live'
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from playwright.async_api import async_playwright
from loguru import logger

# Path to store the authenticated session
AUTH_FILE = os.path.join(ROOT_DIR, 'data/browser_state.json')

async def capture_session():
    """
    Launches a VISIBLE browser for the user to log in manually.
    Once logged in, it saves the session state (cookies/storage) for headless reuse.
    """
    logger.info("🚀 Launching secure browser for Manual Authentication...")
    logger.info("👉 Please log in to your Google Account in the opened window.")
    
    async with async_playwright() as p:
        # Launch non-headless browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Go to Google Sites
        await page.goto("https://sites.google.com")
        
        # Wait for user to log in manually
        logger.info("⏳ Waiting for login... (Look for 'Google Account' avatar or Dashboard)")
        try:
            # Wait for either the "Create new site" button OR the Google Account avatar in the top right
            # "gb_d" class is common for the Google Bar avatar, or aria-label containing "Google Account"
            await page.wait_for_selector('a[aria-label*="Google Account"], div[aria-label="Create new site"], div[data-tooltip="Create new site"]', timeout=300000)
            
            # Give it a few more seconds to settle cookies
            await float.sleep(3) 

            logger.success("✅ Login detected!")
            
            # Save storage state
            await context.storage_state(path=AUTH_FILE)
            logger.success(f"💾 Session saved securely to: {AUTH_FILE}")
            
        except Exception as e:
            logger.error(f"❌ Login timed out or failed: {e}")
            
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_session())
