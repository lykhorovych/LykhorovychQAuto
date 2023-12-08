import pytest
import os.path
import logging

from modules.api.clients.github import GitHub
from modules.common.database import DataBase
from modules.ui.page_objects.amazon.amazon_start_page import AmazonStartPage
from modules.ui.page_objects.rozetka.rozetka_basket_page import RozetkaPage
from modules.ui.page_objects.nova_poshta.nova_poshta_trecking_page import NovaPoshtaTrackingPage
from modules.common.readconfig import ReadConfig

BASE_DIR = ReadConfig.get_base_dir()
logging.basicConfig(level=logging.ERROR, filename=BASE_DIR / "logs" / "py_log.log", filemode="w")

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
def user():
    user = User()
    user.create()

    yield user

    user.remove()


def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default='false', help="run in headless mode")
    parser.addoption("--browser", action="store", default='chrome',
                     help="""'chrome' - for Chrome browser
                             'firefox' - for Mozilla Firefox browser
                             'edge' - for Edge browser""")


@pytest.fixture(scope='class')
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='class')
def headless(request):
    if request.config.getoption("--headless") == 'true':
        return True
    return False


@pytest.fixture
def github_api():
    api = GitHub()

    return api


@pytest.fixture
def database_api():
    api = DataBase()

    yield api

    api.close()

@pytest.fixture(scope='module')
def amazon_page():
    page = AmazonStartPage()
    page.open()

    yield page

    page.close()


@pytest.fixture(scope='function')
def amazon_page_login():
    page = AmazonStartPage()
    page.open()

    yield page

    page.close()


@pytest.fixture(scope='class')
def rozetka_page(browser, headless):
    page = RozetkaPage(browser, headless)
    page.open()

    yield page

    page.close()


@pytest.fixture
def nova_poshta_page():
    page = NovaPoshtaTrackingPage()
    page.open()

    yield page

    page.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        folder = "_".join(item.fixturenames[0].split("_")[:-1])
        driver_fix = {'rozetka_page', 'amazon_page', 'nova_poshta_page'}.intersection(item.fixturenames)
        if driver_fix:
            driver = item.funcargs[driver_fix.pop()]
            driver.driver.save_screenshot(os.path.join(BASE_DIR, f'screenshots\\{folder}\\',
                                                       item.name + '.png'))
        logging.error(f"{item.reportinfo()[2]}:{call.excinfo}")