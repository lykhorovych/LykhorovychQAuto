import requests

from modules.ui.page_objects.rozetka.base_page import BasePage
from modules.ui.page_objects.rozetka.locators import BasketPageLocators
from modules.ui.page_objects.rozetka.undetected import UndetectedDriver

class RozetkaPage(BasePage):
    URL = "https://rozetka.com.ua/ua"

    def open(self):
        super().open(RozetkaPage.URL)

    def input_product_in_search_field(self, product_name: str):
        search_field = self.element_is_visible(BasketPageLocators.SEARCH_FIELD)
        self.send_value_into_input_field(search_field, product_name)

        title = self.title_is_contains(product_name)

        return title

    def add_first_searched_product_to_cart(self):
        cart_btn = self.element_is_clickable(BasketPageLocators.ADD_TO_CART)
        cart_btn.click()

    def check_number_in_icon(self):
        state = self.text_is_present_in_element(BasketPageLocators.ICON_BADGE,
                             "1")  # waiting until a product is added to the cart
        return state

    def open_basket_window(self):
        basket_btn = self.element_is_clickable(BasketPageLocators.CART_LINK)
        basket_btn.click()
        title = self.element_is_visible(BasketPageLocators.BASKET_HEADING)
        return title

    def get_count_of_products_in_cart(self):
        products = self.elements_are_visible(BasketPageLocators.LIST_PRODUCTS)
        return len(products)

    def get_discount_of_price(self):
        discount = self.element_is_visible(BasketPageLocators.DISCOUNT_VALUE)
        discount = int(discount.text[1:-1])  # clearing unnecessary characters and cast type value from str to int
        return 1 - discount / 100
    
    def get_price_before_discount(self):
        old_cost = self.element_is_visible(BasketPageLocators.OLD_COST)
        old_cost = int("".join(old_cost.text[:-1].split()))  # clearing unnecessary characters and cast type value from
                                                             # str to int
        return old_cost

    def get_price_after_discount(self):
        price = self.element_is_visible(BasketPageLocators.COST_WITH_DISCOUNT)
        price = int("".join(price.text[:-1].split()))  # clearing unnecessary characters and cast type value from str to int
        return price

    def add_count_of_product(self, clicks):
        for _ in range(clicks):
            self.element_is_clickable(BasketPageLocators.PLUS_BUTTON).click()

    def decries_count_of_product(self, clicks):
        for _ in range(clicks):
            self.element_is_clickable(BasketPageLocators.MINUS_BUTTON).click()

    def input_count_within_input_field(self, value):
        input_elem = self.element_is_visible(BasketPageLocators.INPUT_FIELD)
        self.send_value_into_input_field(input_elem, value)

        return int(input_elem.get_attribute("value"))

    def check_count_of_products_in_input_field(self, value):
        count = self.value_is_present_in_element(BasketPageLocators.INPUT_FIELD, value)

        return int(count.get_attribute("value"))

    @staticmethod
    def convert_value(value):
        result = ''
        for i, elem in enumerate(str(value)[::-1], 1):
            result += elem
            if i % 3 == 0:
                result += ' '
        order_price = result[::-1].strip()
        return order_price

    def if_final_price_is_valid(self, value):
        order_price = self.text_is_present_in_element(BasketPageLocators.FINAL_PRICE,
                                               value)
        return order_price

    def delete_product_from_cart(self):
        three_dots = self.element_is_clickable(BasketPageLocators.TREE_DOTS_BUTTON)
        three_dots.click()

        delete_btn = self.element_is_clickable(BasketPageLocators.DELETE_BUTTON)
        delete_btn.click()

        cart_heading = self.element_is_visible(BasketPageLocators.CART_MESSAGE)
        return cart_heading.text

    def get_color_of_checkout_button(self):
        checkout_btn = self.element_is_clickable(BasketPageLocators.CHECKOUT_BUTTON)

        color = self.get_value_of_css_property(checkout_btn, 'background-color')

        return color

    def press_close_button_and_return_to_main_window(self):
        close_btn = self.element_is_clickable(BasketPageLocators.CLOSE_BUTTON)
        close_btn.click()

        return self.title_is_contains("Jack Daniel's")

    def check_invisibility_of_badge_icon_on_cart_button(self):
        icon = self.element_is_not_visible(BasketPageLocators.ICON_BADGE)

        return icon