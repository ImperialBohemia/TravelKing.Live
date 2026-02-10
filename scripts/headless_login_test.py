import asyncio
import os
from playwright.async_api import async_playwright

EMAIL = 'trendnatures@gmail.com'
APP_PASS = 'zzpd unbh srxl omvu'
SITE_URL = 'https://sites.google.com/d/1Kc8GEiGzgo2YdyzDViq1T8NXQpipjQwF/edit'
HTML_FILE = '/home/q/TravelKing.Live/index.html'

async def login_and_inject():
    async with async_playwright() as p:
        print("🚀 Starting Headless Login sequence...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        try:
            # 1. Login
            print(f"📧 Logging in as {EMAIL}...")
            await page.goto("https://accounts.google.com/signin", wait_until="networkidle")
            await page.fill('input[type="email"]', EMAIL)
            await page.click('#identifierNext')
            await asyncio.sleep(3)
            
            # Check for password field
            print("🔑 Entering password...")
            await page.wait_for_selector('input[type="password"]', timeout=30000)
            await page.fill('input[type="password"]', APP_PASS)
            await page.click('#passwordNext')
            await asyncio.sleep(5)
            
            # Check if login succeeded or redirected
            if "myaccount.google.com" in page.url or "google.com" in page.url:
                print("✅ Login potentially successful!")
            else:
                print(f"⚠️ Redirected to: {page.url}")
                await page.screenshot(path="login_state.png")
                print("📸 Login state saved.")

            # 2. Go to Site
            print(f"🌐 Navigating to Editor: {SITE_URL}")
            await page.goto(SITE_URL, wait_until="networkidle", timeout=60000)
            await asyncio.sleep(10)
            
            # 3. Check for specific editor elements
            print("🔍 Checking for Editor elements...")
            try:
                # Search for 'Embed' or 'Insert'
                await page.wait_for_selector('div[role="button"][aria-label="Embed"]', timeout=30000)
                print("💎 OMEGA! We are in the editor!")
                # ... same injection logic as before ...
                # (Skipping for brevity in this test log, will add if successful)
            except:
                print("❌ Could not reach Editor UI.")
                await page.screenshot(path="editor_fail.png")

        except Exception as e:
            print(f"❌ Error: {e}")
            await page.screenshot(path="fatal_error.png")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(login_and_inject())
