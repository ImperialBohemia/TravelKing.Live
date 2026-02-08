import requests

def check_status(url):
    """Verify if a page returns an HTTP 200 OK status."""
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Validation error for {url}: {e}")
        return False

if __name__ == "__main__":
    # Test with a known URL
    test_url = "https://google.com"
    print(f"Checking {test_url}: {check_status(test_url)}")
