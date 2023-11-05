import requests
from selenium.webdriver.common.keys import Keys

from modules.ui.page_objects.rozetka.base_page import BasePage
from modules.ui.page_objects.rozetka.locators import BasketPageLocators


class RozetkaBasketPage(BasePage):
    URL = "https://rozetka.com.ua/ua"

    def open(self):
        self.driver.get(RozetkaBasketPage.URL)
        self.driver.maximize_window()

    def jump_to_basket(self):
        basket_elem = self.element_is_clickable(BasketPageLocators.CART_LINK)
        basket_elem.click()
        title = self.element_is_visible(BasketPageLocators.BASKET_HEADING)
        return title

    def search_and_add_product_to_cart(self, name: str):
        search_elem = self.element_is_visible(BasketPageLocators.SEARCH_FIELD)
        search_elem.clear()
        search_elem.send_keys(name)
        search_elem.send_keys(Keys.ENTER)

        btn = self.elements_are_visible(BasketPageLocators.ADD_TO_CART)[0]
        self.driver.implicitly_wait(10)
        search_title = self.driver.title
        btn.click()

        return search_title

    def get_count_products_in_cart(self):
        products = self.elements_are_visible(BasketPageLocators.LIST_PRODUCTS)
        return len(products)

    def get_discount_of_price(self):
        discount = self.element_is_visible(BasketPageLocators.DISCOUNT_VALUE)
        discount = int(discount.text[1:-1])
        return discount / 100
    
    def get_price_before_discount(self):
        old_cost = self.element_is_visible(BasketPageLocators.OLD_COST)
        old_cost = int("".join(old_cost.text[:-1].split()))
        return old_cost

    def get_price_after_discount(self):
        price = self.element_is_visible(BasketPageLocators.COST_WITH_DISCOUNT)
        price = int("".join(price.text[:-1].split()))
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
        input_elem.clear()
        input_elem.send_keys(value)
        input_elem.send_keys(Keys.ENTER)

        return int(input_elem.get_attribute("value"))

    def check_count_of_product_in_input_field(self):
        count = self.element_is_visible(BasketPageLocators.INPUT_FIELD)
        return int(count.get_attribute("value"))

    def get_order_and_price_values(self):
        order = self.element_is_visible(BasketPageLocators.FINAL_PRICE)

        price = self.get_price_after_discount()
        return price, int("".join(order.text[:-1].split()))

    def delete_product_from_cart(self):
        three_dots = self.element_is_clickable(BasketPageLocators.TREE_DOTS_BUTTON)
        three_dots.click()

        delete_btn = self.element_is_clickable(BasketPageLocators.DELETE_BUTTON)
        delete_btn.click()

        cart_heading = self.element_is_visible(BasketPageLocators.CART_MESSAGE)
        return cart_heading.text

    def get_status_code_checkout_button(self):
        checkout_btn = self.element_is_clickable(BasketPageLocators.CHECKOUT_BUTTON)

        res = requests.get(checkout_btn.get_attribute("href"))

        return res.status_code
