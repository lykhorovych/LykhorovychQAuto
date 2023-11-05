import pytest
from modules.ui.page_objects.amazon.amazon_start_page import AmazonStartPage
from modules.ui.page_objects.rozetka.rozetka_basket_page import RozetkaBasketPage
from modules.ui.page_objects.nova_poshta.nova_poshta_trecking_page import NovaPoshtaTrackingPage

class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Oleh"
        self.second_name = "Lykhorovych"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user(request):
    user = User()
    user.create()

    request.addfinalizer(lambda: user.remove())

    return user

@pytest.fixture(scope='module')
def amazon_page(request):
    page = AmazonStartPage()
    page.open()

    request.addfinalizer(page.close)

    return page

@pytest.fixture(scope='function')
def amazon_page_login(request):
    page = AmazonStartPage()
    page.open()

    request.addfinalizer(page.close)

    return page

@pytest.fixture(scope='module')
def rozetka_page(request):
    page = RozetkaBasketPage()
    page.open()

    request.addfinalizer(page.close)

    return page

@pytest.fixture
def nova_poshta_page(request):
    page = NovaPoshtaTrackingPage()
    page.open()

    request.addfinalizer(page.close)

    return page