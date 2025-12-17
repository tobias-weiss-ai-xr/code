import asyncio
from playwright.async_api import async_playwright

async def take_screenshot(symbol: str, output_path: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        url = f"https://finance.yahoo.com/quote/{symbol}/chart?p={symbol}"
        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="load") # Wait until 'load' event is fired

        # Wait for network to be idle, which often means dynamic content has settled
        await page.wait_for_load_state('networkidle')

        # Wait for the specific chart element to be visible with increased timeout
        chart_selector = 'canvas[data-testid="chart-canvas"]'
        try:
            await page.wait_for_selector(chart_selector, timeout=60000) # 60 seconds timeout
            print(f"Chart element found for {symbol}.")
        except Exception as e:
            print(f"Warning: Chart element '{chart_selector}' not found within timeout for {symbol}: {e}")
            chart_element = None # Set to None if not found

        print(f"Taking screenshot of the chart for {symbol}...")
        
        # Locate the chart element again (or use the previous selector if it was found)
        if chart_element := await page.query_selector(chart_selector):
            await chart_element.screenshot(path=output_path)
            print(f"Screenshot saved to {output_path}")
        else:
            print(f"Could not find the chart element for {symbol}. Taking full page screenshot instead.")
            await page.screenshot(path=output_path, full_page=True)
            print(f"Full page screenshot saved to {output_path}")

        await browser.close()

if __name__ == "__main__":
    stock_symbol = "AAPL" # Example symbol
    screenshot_file = "gfx/yahoo_chart_AAPL.png"
    asyncio.run(take_screenshot(stock_symbol, screenshot_file))