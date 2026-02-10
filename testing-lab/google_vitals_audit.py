import requests
from bs4 import BeautifulSoup
import sys

def audit_vitals(url):
    print(f"🕵️ OMEGA Google Vitals Audit: {url}")
    print("-" * 40)

    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')

        # 1. Check Metadata
        title = soup.find('title')
        description = soup.find('meta', attrs={'name': 'description'})

        print(f"SEO Title      : {'✅' if title else '❌ MISSING'}")
        if title: print(f"  -> {title.text}")

        print(f"SEO Description: {'✅' if description else '❌ MISSING'}")

        # 2. Check for Images without Alt text
        images = soup.find_all('img')
        images_missing_alt = [img for img in images if not img.get('alt')]
        print(f"Image Alt Tags : {'✅' if not images_missing_alt else '❌ ' + str(len(images_missing_alt)) + ' MISSING'}")

        # 3. Check for Semantic Headers
        h1 = soup.find_all('h1')
        print(f"H1 Tags        : {'✅' if len(h1) == 1 else '⚠️ ' + str(len(h1)) + ' DETECTED'}")

        # 4. Check for viewport meta
        viewport = soup.find('meta', attrs={'name': 'viewport'})
        print(f"Mobile Viewport: {'✅' if viewport else '❌ MISSING'}")

    except Exception as e:
        print(f"❌ Audit failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 google_vitals_audit.py <url>")
    else:
        audit_vitals(sys.argv[1])
