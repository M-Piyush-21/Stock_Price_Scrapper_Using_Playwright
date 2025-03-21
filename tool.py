from playwright.sync_api import sync_playwright

def google_finance_bot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        page = browser.new_page()

        print("🚀 Opening Google Finance...")
        page.goto("https://www.google.com/finance/quote/NSE:BSE")

        search_box = page.locator('[aria-label="Search for stocks, ETFs & more"]').first
        search_box.click()
        search_box.fill("IRB")
        search_box.press("Enter")

        print("🔎 Searching for Tata Power stock...")


        page.wait_for_timeout(3000)  


        price_locator = page.locator('.YMlKec.fxKbKc')
        page.wait_for_selector('.YMlKec.fxKbKc', timeout=5000)

        price = price_locator.inner_text()

        print(f"💰 Tata Power Stock Price: {price}")

        page.pause()


if __name__ == "__main__":
    google_finance_bot()
