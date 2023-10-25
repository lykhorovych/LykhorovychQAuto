import pytest

from modules.api.clients.github import GitHub
from modules.common.database import DataBase


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


@pytest.fixture
def github_api():
    api = GitHub()

    return api


@pytest.fixture(scope="class")
def database_api(request):
    api = DataBase()

    request.addfinalizer(api.close)

    return api
