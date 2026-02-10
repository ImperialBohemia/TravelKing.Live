
import asyncio
import os
from playwright.async_api import async_playwright

USER_DATA_DIR = '/home/q/TravelKing.Live/tmp_profile/google-chrome'

async def flow_login_probe():
    async with async_playwright() as p:
        print("🚀 Launching Headless Browser for Google Flow Authentication Probe...")
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        page = await context.new_page()
        
        url = 'https://labs.google/fx/tools/flow/'
        print(f"🌐 Navigating to {url}...")
        try:
            await page.goto(url, wait_until="networkidle", timeout=60000)
            await asyncio.sleep(5)
            
            # Click "OK, got it" on cookie banner if present
            cookie_btn = await page.query_selector('button:has-text("OK, got it")')
            if cookie_btn:
                await cookie_btn.click()
                print("🔘 Clicked cookie banner.")
                await asyncio.sleep(1)

            # Click "Create with Flow" to trigger login or project list
            create_btn = await page.query_selector('button:has-text("Create with Flow")')
            if create_btn:
                print("🔘 Clicking 'Create with Flow'...")
                await create_btn.click()
                await asyncio.sleep(8)
            
            await page.screenshot(path="flow_after_click.png")
            print("📸 Checkout flow_after_click.png")
            
            # Final check of the URL and content to see if we reached the internal app
            print(f"📍 Final URL: {page.url}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            await page.screenshot(path="flow_probe_error.png")
        finally:
            await context.close()

if __name__ == "__main__":
    asyncio.run(flow_login_probe())
