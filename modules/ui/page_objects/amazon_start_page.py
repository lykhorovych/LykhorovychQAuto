import time

import requests
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.locators import MainPageLocators


class AmazonStartPage(BasePage):
    URL = "https://www.amazon.com/ref=nav_bb_logo"

    def open(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(AmazonStartPage.URL)

    def try_search_product_in_search_field(self, value, status=False):
        search_field = self.element_is_visible(MainPageLocators.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(value)

        typed_value = search_field.get_attribute("value")

        if not status:
            go_btn = self.element_is_clickable(MainPageLocators.GO_BUTTON)
            go_btn.click()
        else:
            search_field.send_keys(Keys.ENTER)

        return typed_value

    def check_title(self, expected_title):
        print("check title")
        assert self.driver.title == expected_title

    def check_placeholder(self):
        search_field = self.element_is_visible(MainPageLocators.SEARCH_FIELD)
        search_field.clear()
        placeholder = search_field.get_attribute("placeholder")
        return placeholder

    def select_dropdown_box_description_option(self, value):
        select = Select(self.driver.find_element(*MainPageLocators.DROPDOWN_BOX_LINK))
        select.select_by_visible_text(text=value)

        return select.first_selected_option.text

    def move_to_bottom_of_window(self):
        el = self.element_is_clickable(MainPageLocators.BACK_TO_TOP_LINK)
        self.move_to_element(el)

        return el

    @staticmethod
    def get_element_property(element, property):
        return element.value_of_css_property(property)

    def get_button_go_color(self):
        button = self.element_is_visible(MainPageLocators.GO_BUTTON)
        color = AmazonStartPage.get_element_property(button, "background-color")
        return color
