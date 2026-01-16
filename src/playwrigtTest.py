from playwright.sync_api import sync_playwright


def prtSc():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://www.baidu.com")
        page.fill("textarea[id='chat-textarea']", "github")
        page.keyboard.press("Enter")
        page.wait_for_selector("div[id='content_left']")
        page.screenshot(path="google_search_github.png", full_page=True)
        browser.close()

if __name__ == '__main__':
    prtSc()