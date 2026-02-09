import asyncio
import os
import sys
import json

ROOT_DIR = '/home/q/TravelKing.Live'
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from loguru import logger

# Paths
AUTH_FILE = os.path.join(ROOT_DIR, 'data/browser_state.json')
SITE_URL = "https://sites.google.com/d/1Kc8GEiGzgo2YdyzDViq1T8NXQpipjQwF/p/13KiP0UT99cXKiYTBgzHwioVd-IucMCie/edit"

async def manage_site_securely():
    if not os.path.exists(AUTH_FILE):
        logger.error(f"❌ No session file found at {AUTH_FILE}. Run 'scripts/auth_capture.py' first!")
        return

    logger.info("🚀 Starting Headless Manager with SECURE SESSION...")

    async with async_playwright() as p:
        # Load the saved session state
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state=AUTH_FILE)
        page = await context.new_page()
        
        # Apply stealth just in case
        await Stealth().apply_stealth_async(page)

        try:
            logger.info(f"🔗 Navigating to Site Editor: {SITE_URL}")
            await page.goto(SITE_URL, wait_until="networkidle", timeout=60000)
            
            # Check if we are still logged in
            if "accounts.google.com" in page.url:
                logger.error("🛑 Session expired or invalid. Please re-run auth_capture.py.")
                await page.screenshot(path="logs/session_expired.png")
                return

            # Editor Validation
            await page.wait_for_selector('div[aria-label="Publish"]', timeout=30000)
            logger.success("🎯 Connected to Site Editor! Injecting content...")
            
            # 1. Add Hero Title
            # Click "Text box" from right sidebar
            await page.click('span:has-text("Text box")') 
            await page.keyboard.type("Flight Cancelled? Don't Panic.")
            await page.keyboard.press("Enter")
            await page.keyboard.type("We help you get compensation and verify alternative flights instantly.")
            
            # 2. Add Image (Placeholder logic - requires file chooser handling)
            # await page.click('span:has-text("Images")')
            # ... handling file upload is complex in headless often
            
            # 3. Publish
            logger.info("🌍 Publishing changes...")
            await page.click('div[aria-label="Publish"]')
            # Confirm publish if modal appears
            try:
                await page.wait_for_selector('div[role="button"][aria-label="Publish"]', timeout=5000)
                await page.click('div[role="button"][aria-label="Publish"]')
            except:
                pass # Already published or no changes
            
            logger.success("✅ Content Injected & Published!")
            await page.screenshot(path="logs/content_injected.png")

        except Exception as e:
            logger.error(f"💥 ERROR: {e}")
            await page.screenshot(path="logs/secure_error.png")

        except Exception as e:
            logger.error(f"💥 ERROR: {e}")
            await page.screenshot(path="logs/secure_error.png")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(manage_site_securely())
