import time
import requests

from selenium.webdriver import Chrome, ChromeOptions, ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class UndetectedDriver:

    def open(self, url):
        res = requests.get(
            r'http://local.adspower.net:50325/api/v1/browser/start?user_id=jbvjc1a&launch_args='
            fr'["{url}"]&clear_cache_after_closing=1').json()
        time.sleep(6)
        options = ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_experimental_option("debuggerAddress", res['data']['ws']['selenium'])
        driver = Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if driver.current_url == url + "/":
                break
        driver.maximize_window()
        self.driver = driver

    @staticmethod
    def close():
        res = requests.get(r'http://local.adspower.net:50325/api/v1/browser/stop?user_id=jbvjc1a')
        message = res.json()['msg']
        print(message)
