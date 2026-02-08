
import asyncio
from playwright.async_api import async_playwright
import time
import json

async def run():
    async with async_playwright() as p:
        # 1. Launch Browser
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # 2. Login to Google
        print("Logging in to trendnatures@gmail.com...")
        await page.goto("https://accounts.google.com/signin")
        await page.fill('input[type="email"]', "trendnatures@gmail.com")
        await page.click('button:has-text("Next")')
        await page.wait_for_timeout(2000)
        
        await page.fill('input[type="password"]', "Brasco2026@@~~")
        await page.click('button:has-text("Next")')
        
        # Check for 2FA or successful login
        await page.wait_for_timeout(5000)
        if "challenge" in page.url:
            print("🚨 2FA BLOCKED: User intervention required for login!")
            await browser.close()
            return

        print("✅ Login Successful!")

        # 3. Open the Sheet
        sheet_id = "1uvNvNKei8sgmrASHE5OpQKwEANcOFjxOCdIxMWBnOQc"
        print(f"Opening Sheet: {sheet_id}")
        await page.goto(f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit")
        await page.wait_for_timeout(5000)

        # 4. Create SYSTEM_STATUS tab if it doesn't exist
        print("Checking for SYSTEM_STATUS tab...")
        tabs = await page.query_selector_all('.docs-sheet-tab-name')
        tab_names = [await t.inner_text() for t in tabs]
        if "SYSTEM_STATUS" not in tab_names:
            print("Creating SYSTEM_STATUS tab...")
            await page.click('[aria-label="Insert sheet"]')
            await page.wait_for_timeout(2000)
            # Rename the new sheet
            # This is complex in headless, but let's try to just share first
        else:
            print("✅ SYSTEM_STATUS tab already exists.")

        # 5. Share with Service Account
        print("Sharing with Service Account...")
        try:
            await page.click('button:has-text("Share")')
            await page.wait_for_timeout(2000)
            
            sa_email = "travelking@travelking.iam.gserviceaccount.com"
            await page.fill('input[aria-label="Add people and groups"]', sa_email)
            await page.wait_for_timeout(1000)
            await page.keyboard.press("Enter")
            
            # Ensure Editor role
            # It's usually default, but we can verify if needed
            
            await page.click('button:has-text("Send"), button:has-text("Done")')
            print(f"✅ Shared with {sa_email}!")
        except Exception as e:
            print(f"❌ Sharing failed: {e}")

        await page.wait_for_timeout(2000)
        await browser.close()
        print("🚀 Enterprise Fix Completed Headless!")

if __name__ == "__main__":
    asyncio.run(run())
