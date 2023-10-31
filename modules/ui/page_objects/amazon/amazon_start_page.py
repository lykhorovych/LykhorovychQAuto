import time

import requests
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.amazon.locators import MainPageLocators
from modules.common.readconfig import ReadConfig


class AmazonStartPage(BasePage):
    URL = "https://www.amazon.com/ref=nav_bb_logo"
    LOGIN = ReadConfig.get_username()
    PASSWORD = ReadConfig.get_password()

    def open(self):
        self.driver.implicitly_wait(10)
        self.driver.get(AmazonStartPage.URL)
        self.driver.maximize_window()
        self.element_is_clickable(MainPageLocators.LOGO_LINK).click()

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

    def try_log_in(self, login):
        login_link = self.element_is_visible(MainPageLocators.SIGN_IN_LINK)
        link = login_link.get_attribute("href")
        self.driver.switch_to.new_window("Tab")
        self.driver.get(link)

        login_elem = self.element_is_visible(MainPageLocators.LOGIN_FIELD)
        login_elem.send_keys(login)

        con_btn = self.element_is_clickable(MainPageLocators.CONTINUE_BUTTON)
        con_btn.click()

        return login_elem
    def try_input_valid_password(self, password):
        password_elem = self.element_is_visible(MainPageLocators.PASSWORD_FIELD)
        password_elem.send_keys(password)

        sbm_button = self.element_is_clickable(MainPageLocators.SUBMIT_BUTTON)
        sbm_button.click()

    def get_alert_message(self, key):
        message = {
            'missing': lambda: self.element_is_visible(MainPageLocators.ALERT_MISSING),
            'message': lambda: self.element_is_visible(MainPageLocators.ALERT_MESSAGE),
            'heading': lambda: self.element_is_visible(MainPageLocators.ALERT_HEADING)
        }
        return message[key]()
    
    def open_account_and_lists_block(self):
        self.driver.execute_script("document.getElementById('nav-flyout-accountList').\
                                   style.display='block';")
    
    def get_list_of_links(self):
        lists = self.elements_are_visible(MainPageLocators.LISTS_LINKS)
        account_links = self.elements_are_visible(MainPageLocators.ACCOUNT_LINKS)
        return lists + account_links        

    def create_new_wishlist(self, list_name: str):
        outer_link = self.element_is_clickable(MainPageLocators.CREATE_LIST_OUTER_LINK)
        outer_link.click()
        inner_link = self.element_is_clickable(MainPageLocators.CREATE_LIST_INNER_LINK)
        inner_link.click()
        header = self.element_is_visible(MainPageLocators.CREATE_LIST_HEADER).text
        list_name_field = self.element_is_visible(MainPageLocators.CREATE_LIST_INPUT)
        list_name_field.clear()
        list_name_field.send_keys(list_name)

        create_list_button = self.element_is_clickable(MainPageLocators.CREATE_LIST_BUTTON)
        create_list_button.click()

        return header

    def count_elements_in_list(self):
        count_of_lists = self.elements_are_visible(MainPageLocators.SHOPPING_LISTS)
        return count_of_lists
