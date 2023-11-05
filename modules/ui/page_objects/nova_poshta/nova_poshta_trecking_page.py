from modules.ui.page_objects.nova_poshta.base_page import BasePage
from modules.ui.page_objects.nova_poshta.locators import NovaPoshtaTrackingPageLocators
from selenium.webdriver.common.keys import Keys

class NovaPoshtaTrackingPage(BasePage):
    URL = "https://tracking.novaposhta.ua/#/uk"

    def open(self):
        self.driver.get(url=self.URL)
        self.driver.maximize_window()

    def check_title(self):
        title = self.driver.title

        assert "Керуйте доставкою посилок Нової пошти" == title

    def type_number_of_invoice_into_search_field(self, number: str):
        elem = self.element_is_visible(NovaPoshtaTrackingPageLocators.INPUT_FIELD)
        elem.clear()
        elem.send_keys(number)
        elem.send_keys(Keys.ENTER)
        return elem
    
    def click_on_clear_sign_into_search_field(self):
        elem = self.element_is_visible(NovaPoshtaTrackingPageLocators.TRACKING_CLOSE_SIGN)
        elem.click()
        
    @staticmethod    
    def get_elem_attribute(elem, attr):
        return elem.get_attribute(attr)

    @staticmethod
    def get_elem_css_property(elem, property):
        return elem.value_of_css_property(property)

    def get_search_button_properties(self):
        btn = self.element_is_visible(NovaPoshtaTrackingPageLocators.SEARCH_BUTTON)
        disabled = self.get_elem_attribute(btn, "disabled")

        color = self.get_elem_css_property(btn, "background-color")
        return disabled, color