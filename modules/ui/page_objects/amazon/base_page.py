from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from config.config import BASE_DIR


class BasePage:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def close(self):
        self.driver.close()

    def element_is_present(self, locator, timeout=10):
        try:
            element = WebDriverWait(timeout=timeout, driver=self.driver).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            self.driver.save_screenshot(
                BASE_DIR / f"screenshots/amazon/{self.driver.current_url}.png")
            self.driver.close()

    def elements_are_present(self, locator, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except (NoSuchElementException, TimeoutException):
            self.driver.save_screenshot(
                BASE_DIR / f"screenshots/amazon/{self.driver.current_url}.png")
            self.driver.close()

    def element_is_visible(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            self.driver.save_screenshot(
                BASE_DIR / f"screenshots/amazon/{self.driver.current_url}.png")
            self.driver.close()

    def elements_are_visible(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            self.driver.save_screenshot(
                BASE_DIR / f"screenshots/amazon/{self.driver.current_url}.png")
            self.driver.close()

    def element_is_not_visible(self, locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            self.driver.save_screenshot(
                BASE_DIR / f"screenshots/amazon/{self.driver.current_url}.png")
            self.driver.close()

    def element_is_clickable(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            self.driver.save_screenshot(
                BASE_DIR / f"screenshots/amazon/{self.driver.current_url}.png")
            self.driver.close()

    def move_to_element(self, element):  #
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_element_on_focus(self, element):
        self.driver.execute_script("arguments[0].focus();", element)
