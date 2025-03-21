**Srock Price Scrapper Using Playwright**

## Introduction
This documentation provides an overview of a web scraper tool built using Playwright. Playwright is a powerful automation library that enables browser interaction for web scraping, testing, and automation. This tool is designed to extract stock prices from Google Finance and take screenshots for verification.

## Prerequisites
Before using this tool, ensure you have the following installed:
- Python (version 3.7 or higher)
- Playwright for Python
- A modern browser (Chromium, Firefox, or WebKit)

### Installation
To install Playwright, run the following command:
```bash
pip install playwright
```

After installation, install the necessary browsers:
```bash
playwright install
```

## Features
- Automates browser interaction using Playwright.
- Searches for stock prices on Google Finance.
- Extracts the stock price and displays it.
- Captures screenshots for validation.
- Runs in both headless and non-headless modes.


## How It Works
1. Opens the Google Finance website.
2. Finds the search input field using the aria-label.
3. Searches for "Tata Power" and presses Enter.
4. Waits for the stock price to load.
5. Extracts the stock price from the relevant HTML element.
6. Captures and saves a screenshot.
7. Closes the browser.

## Usage
Run the script using:
```bash
python tool.py
```

## Notes
- If the script fails to locate elements, verify the HTML structure using the browser's developer tools.
- Increase timeout duration if pages take longer to load.
- Ensure Playwright is installed and up to date.

## Conclusion
This Playwright web scraper efficiently extracts stock prices and captures screenshots for verification. It can be adapted for other websites and automation tasks. Happy scraping!

