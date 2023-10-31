import pytest
import requests

from config.config import BASE_DIR
class TestAmazonStartPage:

    @pytest.mark.skip
    @pytest.mark.new
    def test_open_start_page(self, amazon_page):
        amazon_page.check_title("Amazon.com. Spend less. Smile more.")

    @pytest.mark.skip
    @pytest.mark.new
    def test_placeholder_search_field(self, amazon_page):
        placeholder = amazon_page.check_placeholder()

        assert placeholder == "Search Amazon"

    @pytest.mark.skip
    @pytest.mark.new
    @pytest.mark.parametrize("status", [False, True])
    def test_search_with_all_department_selected(self, amazon_page, status):
        """There is a checking search operation by pressing the button or pressing the ENTER key:
        False means pressing the Go button
        True means pressing the ENTER key"""

        typed_value = amazon_page.try_search_product_in_search_field(
        "iphone", status=status
        )

        assert typed_value == "iphone"
        amazon_page.check_title("Amazon.com : iphone")

    @pytest.mark.skip
    @pytest.mark.new
    @pytest.mark.parametrize(
        "department, value, expected_title",
        [
            [
                "Digital Music",
                "the last shadow puppets",
                "Amazon.com : the last shadow puppets",
            ],
            ["Books", "fluent python", "Amazon.com : fluent python"],
            ["Computers", "amd ryzen 7", "Amazon.com : amd ryzen 7"],
            ["Movies & TV", "Mister Robot", "Amazon.com : Mister Robot"],
        ],
    )
    def test_search_with_selected_department(
        self, amazon_page, department, value, expected_title
    ):
        dropdown_box_option = amazon_page.select_dropdown_box_description_option(department)
        assert dropdown_box_option == department

        typed_value = amazon_page.try_search_product_in_search_field(value)
        assert typed_value == value

        amazon_page.check_title(expected_title)

    @pytest.mark.skip
    @pytest.mark.new
    def test_back_to_top_button(self, amazon_page):
        button = amazon_page.move_to_bottom_of_window()
        amazon_page.driver.save_screenshot(
            BASE_DIR / "test_back_to_top_move_to_bottom.png")
        button.click()
        amazon_page.driver.save_screenshot(
            BASE_DIR / "test_back_to_top_move_to_top.png")

    @pytest.mark.skip
    @pytest.mark.new
    def test_color_of_button_go(self, amazon_page):
        color = amazon_page.get_button_go_color()
        expected_color = "rgba(254, 189, 105, 1)"

        assert color == expected_color

    @pytest.mark.skip
    @pytest.mark.new
    @pytest.mark.parametrize(
        "login, expected_heading, expected_message",
        [
            ("+380505050505", "Incorrect phone number", "We cannot find an account with that mobile number",),
            # check log in with unknown phone number
            ("sven16603.gmail.com", "There was a problem", "We cannot find an account with that email address"),
            # check log in with unknown login
        ],
    )
    def test_login_with_incorrect_login(self, amazon_page_login, login, expected_heading,
                                        expected_message):
        amazon_page_login.try_log_in(login)
        alert_heading = amazon_page_login.get_alert_message('heading').text
        alert_message = amazon_page_login.get_alert_message('message').text

        assert alert_heading == expected_heading
        assert alert_message == expected_message

    @pytest.mark.skip
    @pytest.mark.new
    def test_log_in_with_empty_login(self, amazon_page_login, login="",
                                 expected_message="Enter your email or mobile phone number"):
        login_elem = amazon_page_login.try_log_in(login)
        alert_message = amazon_page_login.get_alert_message('missing').text
        amazon_page_login.driver.implicitly_wait(10)
        border_color = amazon_page_login.get_element_property(login_elem, property="border-color")

        assert alert_message == expected_message
        assert border_color == 'rgb(204, 12, 57)'


    @pytest.mark.new
    def test_correct_login(self, amazon_page):
        amazon_page.try_log_in(amazon_page.LOGIN)

        amazon_page.try_input_valid_password(amazon_page.PASSWORD)

        amazon_page.check_title("Amazon.com. Spend less. Smile more.")

    @pytest.mark.skip
    @pytest.mark.new
    def test_account_link_and_item(self, amazon_page):
        amazon_page.open_account_and_lists_block()
        links = amazon_page.get_list_of_links()
        for link in links:
            print(link.text)
            url = link.get_attribute("href")
            res = requests.get(url)
            assert res.status_code == 200

    @pytest.mark.skip
    @pytest.mark.new
    def test_create_new_wishlist(self, amazon_page):
        amazon_page.open_account_and_lists_block()
        header = amazon_page.create_new_wishlist('Test List')

        assert header == "Create a new list"

        title_list = amazon_page.count_elements_in_list()[0].text
        assert 'Test List' in title_list

    def test_add_product_to_wishlist(self, amazon_page):
        searched_product = amazon_page.try_search_product_in_search_field(
            "iphone", status=False
        )

        assert typed_value == "iphone"
        amazon_page.check_title("Amazon.com : iphone")

    def test_add_product_to_cart_list(self, amazon_page):
        pass

    def test_move_product_to_another_wishlist(self, amazon_page):
        pass

    def test_delete_product_from_wishlist(self, amazon_page):
        pass


