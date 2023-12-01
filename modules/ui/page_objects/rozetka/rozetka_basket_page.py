import requests

from modules.ui.page_objects.rozetka.base_page import BasePage
from modules.ui.page_objects.rozetka.locators import BasketPageLocators
from modules.ui.page_objects.rozetka.undetected import UndetectedDriver

class RozetkaPage(UndetectedDriver, BasePage):
    URL = "https://rozetka.com.ua/ua"

    def open(self):
        super().open(RozetkaPage.URL)

    def input_product_in_search_field(self, product_name: str):
        search_field = self.element_is_visible(BasketPageLocators.SEARCH_FIELD)
        self.send_value_into_input_field(search_field, product_name)

        title = self.title_is_contains(product_name)

        return title

    def search_product_and_add_it_to_cart(self, name: str):
        self.input_product_in_search_field(product_name=name)

        cart_btn = self.element_is_visible(BasketPageLocators.ADD_TO_CART)
        cart_btn.click()

    def open_basket_window(self):
        self.text_in_element_is_present(BasketPageLocators.ICON_BADGE,
                             "1")  # waiting until a product is added to the cart
        basket_btn = self.element_is_clickable(BasketPageLocators.CART_LINK)
        basket_btn.click()
        title = self.element_is_visible(BasketPageLocators.BASKET_HEADING)
        return title

    def get_count_products_in_cart(self):
        products = self.elements_are_visible(BasketPageLocators.LIST_PRODUCTS)
        return len(products)

    def get_discount_of_price(self):
        discount = self.element_is_visible(BasketPageLocators.DISCOUNT_VALUE)
        discount = int(discount.text[1:-1])  # clearing unnecessary characters and cast type value from str to int
        return discount
    
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
        plus_btn = self.element_is_clickable(BasketPageLocators.PLUS_BUTTON)
        for _ in range(clicks):
            plus_btn.click()

    def decries_count_of_product(self, clicks):
        minus_btn = self.element_is_clickable(BasketPageLocators.MINUS_BUTTON)
        for _ in range(clicks):
            minus_btn.click()

    def input_count_within_input_field(self, value):
        input_elem = self.element_is_visible(BasketPageLocators.INPUT_FIELD)
        self.send_value_into_input_field(input_elem, value)
        self.driver.refresh()

        return int(input_elem.get_attribute("value"))

    def check_count_of_products_in_input_field(self):
        count = self.element_is_visible(BasketPageLocators.INPUT_FIELD)
        return int(count.get_attribute("value"))

    def get_order_value(self):
        order = self.element_is_visible(BasketPageLocators.FINAL_PRICE)
        order = int("".join(order.text[:-1].split()))

        return order

    def delete_product_from_cart(self):
        three_dots = self.element_is_clickable(BasketPageLocators.TREE_DOTS_BUTTON)
        three_dots.click()

        delete_btn = self.element_is_clickable(BasketPageLocators.DELETE_BUTTON)
        delete_btn.click()

        cart_heading = self.element_is_visible(BasketPageLocators.CART_MESSAGE)
        return cart_heading.text

    def get_status_code_checkout_button(self):
        checkout_btn = self.element_is_clickable(BasketPageLocators.CHECKOUT_BUTTON)

        res = requests.get(self.get_attribute_value(checkout_btn, "href"))

        return res.status_code
