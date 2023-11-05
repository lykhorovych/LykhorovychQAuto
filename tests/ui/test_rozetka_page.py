import time

import pytest
from config.config import BASE_DIR

class TestRozetkaBasket:

    @pytest.mark.rztk
    def test_add_product_to_basket(self, rozetka_page):
        title = rozetka_page.search_and_add_product_to_cart("Jack Daniel's")

        assert "Jack Daniel's" in title

        rozetka_page.jump_to_basket() # go to basket
        rozetka_page.driver.save_screenshot(BASE_DIR /
                                        'screenshots/rozetka/test_add_product_to_basket.png')

        count = rozetka_page.get_count_products_in_cart()
        assert count == 1

    @pytest.mark.xfail
    @pytest.mark.rztk
    def test_check_discount_price(self, rozetka_page):
        discount = rozetka_page.get_discount_of_price()
        old_price = rozetka_page.get_price_before_discount()
        price = rozetka_page.get_price_after_discount()

        assert old_price * (100-discount)/100 == price# incorrectly calculated the price after the discount on 1 UAH
    @pytest.mark.parametrize("number_of_clicks,expected_count", [(1,2), (2,4), (3,7)])
    @pytest.mark.rztk
    def test_increase_count_of_product_with_plus_sign(self, rozetka_page, number_of_clicks,
                                                      expected_count):
        rozetka_page.add_count_of_product(number_of_clicks)

        count = rozetka_page.check_count_of_product_in_input_field()

        assert count == expected_count

    @pytest.mark.parametrize("number_of_clicks,expected_count", [(3, 4), (2, 2), (1, 1)])
    @pytest.mark.rztk
    def test_reduction_count_of_product_with_minus_sign(self, rozetka_page, number_of_clicks,
                                                        expected_count):
        rozetka_page.decries_count_of_product(number_of_clicks)

        count = rozetka_page.check_count_of_product_in_input_field()

        assert count == expected_count

    @pytest.mark.rztk
    def test_change_count_of_product_and_order_value(self, rozetka_page):
        price, _ = rozetka_page.get_order_and_price_values()# price before change

        count = rozetka_page.input_count_within_input_field(10)# change value to 10

        time.sleep(1)
        _, order = rozetka_page.get_order_and_price_values()# order value with changes

        assert price * count == order # checking the correctness of the order value

    @pytest.mark.rztk
    def test_checkout_button(self, rozetka_page):
        ch_status_code = rozetka_page.get_status_code_checkout_button()

        assert ch_status_code == 200

    @pytest.mark.rztk
    def test_delete_product_from_basket(self, rozetka_page):
        message = rozetka_page.delete_product_from_cart()

        rozetka_page.driver.save_screenshot(BASE_DIR /
                                            'screenshots/rozetka/test_delete_product_from_basket.png')
        assert message == "Кошик порожній"