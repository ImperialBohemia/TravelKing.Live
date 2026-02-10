import asyncio
import os
import sys
from playwright.async_api import async_playwright
from datetime import datetime

# Setup directories
SCREENSHOT_DIR = "testing-lab/reports/screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

async def capture_eyes(url, mode="desktop"):
    """
    OMEGA Visual Eye: Captures full-page screenshots to detect UI flaws.
    Modes: 'desktop' (1920x1080), 'mobile' (iPhone 13 Pro)
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{mode}_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_DIR, filename)

    async with async_playwright() as p:
        print(f"👁️  OMEGA Eye: Opening {url} in {mode} mode...")

        if mode == "mobile":
            device = p.devices["iPhone 13 Pro"]
            browser = await p.webkit.launch()
            context = await browser.new_context(**device)
        else:
            browser = await p.chromium.launch()
            context = await browser.new_context(viewport={"width": 1920, "height": 1080})

        page = await context.new_page()

        try:
            # Navigate with a generous timeout for local dev servers
            await page.goto(url, wait_until="networkidle", timeout=60000)

            # Wait for any lazy animations to settle
            await asyncio.sleep(2)

            print(f"📸 Capturing full page screenshot...")
            await page.screenshot(path=filepath, full_page=True)
            print(f"✅ Screenshot saved: {filepath}")

        except Exception as e:
            print(f"❌ Visual Eye Error: {e}")
        finally:
            await browser.close()

    return filepath

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="OMEGA Visual Eye")
    parser.add_argument("url", help="URL to inspect")
    parser.add_argument("--mode", choices=["desktop", "mobile"], default="desktop", help="View mode")

    args = parser.parse_args()
    asyncio.run(capture_eyes(args.url, args.mode))
