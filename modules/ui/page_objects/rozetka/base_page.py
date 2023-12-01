from selenium.webdriver import Chrome, ChromeOptions, ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Firefox, FirefoxOptions, FirefoxService
from selenium.webdriver import Edge, EdgeService, EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, browser, url, headless=False):
        self.browser = browser
        self.url = url
        self.headless = headless
        self.driver = self.select_driver()

    def chrome_driver(self):
        options = ChromeOptions()
        options.add_argument("--disable-notifications")
        if self.headless:
            options.headless = True
        return Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def firefox_driver(self):
        options = FirefoxOptions()
        options.add_argument("--disable-notifications")
        if self.headless:
            options.headless = True

        return Firefox(service=FirefoxService(), options=options)

    def edge_driver(self):
        options = EdgeOptions()
        options.add_argument("--disable-notifications")
        if self.headless:
            options.use_chromium = True
            options.add_argument("--headless")
            options.add_argument("disable-gpu")

        return Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    def select_driver(self):
        if self.browser == 'chrome':
            return self.chrome_driver()
        elif self.browser == 'edge':
            return self.edge_driver()
        elif self.browser == 'firefox':
            return self.firefox_driver()

    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def close(self):
        self.driver.close()

    def element_is_present(self, locator, timeout=30):
        try:
            element = WebDriverWait(timeout=timeout, driver=self.driver).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def elements_are_present(self, locator, timeout=30):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except (NoSuchElementException, TimeoutException):
            return False

    def element_is_visible(self, locator, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def elements_are_visible(self, locator, timeout=60):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def element_is_not_visible(self, locator, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def element_is_clickable(self, locator, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def title_is_contains(self, title, timeout=30):
        try:
            title = WebDriverWait(self.driver, timeout).until(EC.title_contains(title))
            return title
        except (NoSuchElementException, TimeoutException):
            return False

    def wait_for_change_attribute_value(self, locator, attribute, text, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(
                locator=locator,
                attribute_=attribute,
                text_=text))
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def text_in_element_is_present(self, locator, text, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(
                locator=locator,
                text_=text))
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def send_value_into_input_field(element, value):
        element.clear()
        element.send_keys(value)
        element.send_keys(Keys.ENTER)

    @staticmethod
    def get_attribute_value(element, attribute):
        element.get_attribute(attribute)

    def click_on_btn(self, element):
        self.driver.execute_script("arguments[0].click();", element)
