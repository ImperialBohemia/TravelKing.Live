
import asyncio
import os
from playwright.async_api import async_playwright

USER_DATA_DIR = '/home/q/TravelKing.Live/tmp_profile/google-chrome'

async def probe_flow():
    async with async_playwright() as p:
        print("🚀 Launching Headless Browser for Google Flow Probe...")
        context = await p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )
        page = await context.new_page()
        
        url = 'https://labs.google/flow/'
        print(f"🌐 Navigating to {url}...")
        try:
            await page.goto(url, wait_until="networkidle", timeout=60000)
            await asyncio.sleep(5)
            
            # Take a screenshot to see where we are
            await page.screenshot(path="flow_probe.png")
            print("📸 Screenshot saved to flow_probe.png")
            
            # Check for specific models or text
            content = await page.content()
            if "Nano Banana" in content or "Imagen" in content:
                print("🔍 Found 'Nano Banana' or 'Imagen' in page content!")
            else:
                print("⚠️ 'Nano Banana' not found in raw content.")
                
            # List button labels or interactive elements
            buttons = await page.query_selector_all('button')
            for btn in buttons:
                text = await btn.inner_text()
                if text.strip():
                    print(f"🔘 Button: {text.strip()}")
            
        except Exception as e:
            print(f"❌ Error during probe: {e}")
            await page.screenshot(path="flow_error.png")
        finally:
            await context.close()

if __name__ == "__main__":
    asyncio.run(probe_flow())
