import asyncio
import os
from playwright.async_api import async_playwright

USER_DATA_DIR = '/home/q/TravelKing.Live/tmp_profile'
# If we copied the whole folder, the Default might be inside or it might be the folder itself
if os.path.isdir(os.path.join(USER_DATA_DIR, 'google-chrome')):
    USER_DATA_DIR = os.path.join(USER_DATA_DIR, 'google-chrome')

SITE_URL = 'https://sites.google.com/d/1Kc8GEiGzgo2YdyzDViq1T8NXQpipjQwF/edit'
GAS_SETTINGS_URL = 'https://script.google.com/home/usersettings'
HTML_FILE = '/home/q/TravelKing.Live/index.html'

async def omega_deploy():
    with open(HTML_FILE, 'r') as f:
        html_code = f.read()

    async with async_playwright() as p:
        print("🚀 Launching Headless Omega Browser...")
        # Note: We use the copied profile to bypass login
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        page = await context.new_page()
        
        # 1. Enable Apps Script API (Just in case)
        print(f"⚙️ Checking Apps Script Settings: {GAS_SETTINGS_URL}")
        try:
            await page.goto(GAS_SETTINGS_URL, wait_until="networkidle", timeout=60000)
            await asyncio.sleep(5)
            # Find the toggle for "Google Apps Script API"
            # It usually has text "Google Apps Script API" and a switch
            toggle = await page.query_selector('div[role="switch"]:has-text("Google Apps Script API"), .settings-item-container:has-text("Google Apps Script API") div[role="switch"]')
            if toggle:
                is_on = await toggle.get_attribute("aria-checked") == "true"
                if not is_on:
                    print("🔘 Turning on Apps Script API...")
                    await toggle.click()
                    await asyncio.sleep(2)
                    print("✅ Apps Script API Enabled Headless!")
                else:
                    print("✅ Apps Script API was already Enabled.")
            else:
                print("⚠️ Could not find Apps Script API toggle (already enabled or different UI).")
        except Exception as e:
            print(f"ℹ️ Apps Script settings check skipped/failed: {e}")

        # 2. Inject into Google Site
        print(f"🌐 Navigating to Site Editor: {SITE_URL}")
        try:
            await page.goto(SITE_URL, wait_until="networkidle", timeout=60000)
            await asyncio.sleep(5)
            
            # Click 'Embed'
            print("📦 Inserting Embed...")
            embed_btn = await page.wait_for_selector('div[role="button"][aria-label="Embed"]', timeout=30000)
            await embed_btn.click()
            await asyncio.sleep(2)
            
            # Click 'Embed code' tab
            await page.click('div[role="tab"]:has-text("Embed code")')
            await asyncio.sleep(2)
            
            # Paste HTML code
            print("✂️ Pasting Content...")
            await page.fill('textarea[aria-label="Embed code"]', html_code)
            await asyncio.sleep(2)
            
            # Click 'Next'
            await page.click('div[role="button"]:has-text("Next")')
            await asyncio.sleep(5) # Wait for preview
            
            # Click 'Insert'
            await page.click('div[role="button"]:has-text("Insert")')
            await asyncio.sleep(3)
            print("✅ Content Inserted.")
            
            # 3. Publish
            print("🚀 Publishing Site...")
            publish_btn = await page.wait_for_selector('div[role="button"][aria-label="Publish"]', timeout=30000)
            await publish_btn.click()
            await asyncio.sleep(3)
            
            # Confirm publish
            confirm = await page.query_selector('div[role="button"][data-tooltip="Publish"]:has-text("Publish")')
            if confirm:
                await confirm.click()
                await asyncio.sleep(5)
            
            print("🎉 SUCCESS! Web is LIVE on Google Sites.")

        except Exception as e:
            print(f"❌ Site Injection Error: {e}")
            await page.screenshot(path="error_screenshot.png")
            print("📸 Error screenshot saved to error_screenshot.png")
        finally:
            await context.close()

if __name__ == "__main__":
    asyncio.run(omega_deploy())
