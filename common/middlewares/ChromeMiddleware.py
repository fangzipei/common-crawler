from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType

from rotating_proxies.middlewares import BanDetectionMiddleware
from common.settings import *


class ChromeMiddleware(BanDetectionMiddleware):
    def __init__(self, stats, policy):
        super().__init__(stats=stats, policy=policy)
        self.chrome_path = CHROME_PATH
        self.chrome_user_data_dir = CHROME_USER_DATA_DIR

        chrome_options = Options()
        # chrome_options.add_argument(f'user-data-dir={CHROME_USER_DATA_DIR}')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        chrome_capabilities = DesiredCapabilities.CHROME.copy()
        chrome_capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}

        self.driver = webdriver.Chrome(
            executable_path=CHROME_PATH,
            chrome_options=chrome_options,
            desired_capabilities=chrome_capabilities,
        )

    def process_request(self, request, spider):
        self.driver.get(request.url)

        body = to_bytes(self.driver.page_source)
        return HtmlResponse(
            self.driver.current_url,
            body=body,
            encoding='utf-8',
            request=request,
        )

    def spider_closed(self, spider):
        self.driver.quit()

    def __del__(self):
        self.driver.quit()
