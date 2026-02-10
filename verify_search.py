from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://localhost:3000")

    # Wait for hydration/rendering
    print("Waiting for page load...")
    page.wait_for_selector("text=Origin Port", timeout=10000)

    # 1. Verify Accessibility (Labels linked to inputs)
    print("Verifying accessibility...")
    origin_input = page.get_by_label("Origin Port")
    dest_input = page.get_by_label("Destination Target")
    expect(origin_input).to_be_visible()
    expect(dest_input).to_be_visible()

    # 2. Test Swap Functionality
    print("Testing swap functionality...")
    origin_input.fill("PRG")
    dest_input.fill("DXB")

    # Click swap button
    swap_btn = page.get_by_label("Swap locations")
    expect(swap_btn).to_be_visible()
    swap_btn.click()

    # Verify values swapped
    expect(origin_input).to_have_value("DXB")
    expect(dest_input).to_have_value("PRG")
    print("Swap successful!")

    # 3. Test Error State
    print("Testing error state...")
    origin_input.fill("")
    dest_input.fill("")

    analyze_btn = page.get_by_role("button", name="Analyze Flights")
    analyze_btn.click()

    # Check for red border (class 'border-red-500')
    # Since class names are dynamic, we check if the input has the class
    # Wait for re-render if needed
    page.wait_for_timeout(500)

    # Check if origin input has the error class
    # We can check the class attribute directly or visually via screenshot
    # Let's check class attribute for robustness in script, but screenshot is key
    origin_class = origin_input.get_attribute("class")
    if "border-red-500" in origin_class:
        print("Error state verified: border-red-500 present on origin")
    else:
        print(f"Error state NOT found on origin. Class: {origin_class}")

    dest_class = dest_input.get_attribute("class")
    if "border-red-500" in dest_class:
        print("Error state verified: border-red-500 present on destination")
    else:
        print(f"Error state NOT found on destination. Class: {dest_class}")

    # Take screenshot
    page.screenshot(path="verification.png")
    print("Screenshot saved to verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
