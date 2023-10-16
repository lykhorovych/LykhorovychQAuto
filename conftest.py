import os

import pytest
from dotenv import load_dotenv
from github import Auth, Gist

load_dotenv()


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
    token = os.getenv("GITHUB_TOKEN")
    auth = Auth.Token(token=token)
    gist = Gist.__doc__

    return gist
