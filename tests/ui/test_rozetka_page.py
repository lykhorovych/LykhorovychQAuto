import pytest

class TestRozetkaBasket:

    @pytest.mark.rztk
    def test_search_field(self, rozetka_page):
        page_title = rozetka_page.input_product_in_search_field("Jack Daniel's")

        assert page_title is True

    @pytest.mark.rztk
    def test_visibility_number_of_products_in_cart_icon(self, rozetka_page):
        rozetka_page.add_first_searched_product_to_cart()
        number_in_cart_icon = rozetka_page.check_number_in_icon()

        assert number_in_cart_icon is True

    @pytest.mark.rztk
    def test_add_product_to_basket(self, rozetka_page):
        rozetka_page.open_basket_window()  # go to the basket modal window
        count_product_in_basket = rozetka_page.get_count_of_products_in_cart()

        assert count_product_in_basket != 0

    @pytest.mark.xfail
    @pytest.mark.rztk
    def test_check_discount_price(self, rozetka_page):
        discount = rozetka_page.get_discount_of_price()  # get the discount value
        old_price = rozetka_page.get_price_before_discount()  # get the price before discount
        price = rozetka_page.get_price_after_discount()  # get the price after discount

        assert old_price * discount == price

    @pytest.mark.parametrize("number_of_clicks,expected_count", [(1,2), (2,4), (3,7)])
    @pytest.mark.rztk
    def test_increase_count_of_product_with_plus_sign(self, rozetka_page, number_of_clicks,
                                                      expected_count):

        rozetka_page.add_count_of_product(number_of_clicks)

        count = rozetka_page.check_count_of_products_in_input_field(expected_count)

        assert count == expected_count

    @pytest.mark.parametrize("number_of_clicks,expected_count", [(3, 4), (2, 2), (1, 1)])
    @pytest.mark.rztk
    def test_reduction_count_of_product_with_minus_sign(self, rozetka_page, number_of_clicks,
                                                        expected_count):

        rozetka_page.decries_count_of_product(number_of_clicks)

        count = rozetka_page.check_count_of_products_in_input_field(expected_count)

        assert count == expected_count

    @pytest.mark.rztk
    def test_change_order_value_after_change_product_count(self, rozetka_page, product_count=10):
        price_before_change = rozetka_page.get_price_after_discount()  # price before change

        rozetka_page.input_count_within_input_field(product_count)  # change value to 10

        count = rozetka_page.check_count_of_products_in_input_field(product_count)

        assert count == product_count

        assert rozetka_page.if_final_price_is_valid(
            rozetka_page.convert_value(price_before_change * product_count)
        ) is True

    @pytest.mark.rztk
    def test_green_color_in_checkout_button_is_present(self, rozetka_page):
        ch_button_color = rozetka_page.get_color_of_checkout_button()

        assert ch_button_color == 'rgba(0, 160, 70, 1)'

    @pytest.mark.rztk
    def test_delete_product_from_cart(self, rozetka_page):
        message = rozetka_page.delete_product_from_cart()

        assert message == "Кошик порожній"

    @pytest.mark.rztk
    def test_close_cart_window(self, rozetka_page):
        main_page_title = rozetka_page.press_close_button_and_return_to_main_window()

        assert main_page_title is True

    @pytest.mark.rztk
    def test_not_visibility_badge_on_cart_button(self, rozetka_page):
        not_visibility_badge_on_cart_button = (rozetka_page.
                                               check_invisibility_of_badge_icon_on_cart_button())

        assert not_visibility_badge_on_cart_button is True

