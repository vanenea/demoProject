import asyncio
import random

from playwright.async_api import async_playwright, BrowserContext

from src import config
from src.tools import utils
from src.tools.cdp_browser import CDPBrowserManager


class LvChengCrawler():
    def __init__(self) -> None:
        self.cookie_dict = None
        self.default_headers = None
        self.search_url = None
        self.new_page = None
        self.browser_context = None
        self.index_url = "https://lcfw.yunxuetang.cn/main/#/index"
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        self.cdp_manager = None


    async def start(self):
        async with async_playwright() as playwright:
            self.cdp_manager = CDPBrowserManager()
            self.browser_context = await self.cdp_manager.launch_and_connect(
                playwright,
                None,
                self.user_agent,
                headless=False,
            )
            self.new_page = await self.browser_context.new_page()
            await self.new_page.goto(self.index_url, wait_until="domcontentloaded")
            await self.new_page.fill("input[type='text'][name='username']", config.UN)
            await self.new_page.fill("input[type='password']", config.PD)
            await self.new_page.locator("span:has-text('已阅读并同意')").nth(2).click()
            await self.new_page.locator("span:has-text('登 录')").nth(2).click()
            self.search_url = f"https://api-phx-ali.yunxuetang.cn/sls/contents/search?0={random.random()}"
            await asyncio.sleep(5)
            await self.update_cookies(self.browser_context)
            response = await self.browser_context.request.get(self.search_url)
            print(response.status)
            print(response.json())


    async def update_cookies(self, browser_context: BrowserContext):
        cookie_str, cookie_dict = utils.convert_cookies(await browser_context.cookies())
        self.default_headers["cookie"] = cookie_str
        self.cookie_dict = cookie_dict


    # def getPDF():


if __name__ == '__main__':
    asyncio.run(LvChengCrawler().start())