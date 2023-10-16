import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get("https://api.github.com/zen")
    print(f"Response is {r.text}")


@pytest.mark.http
def test_second_request():
    r = requests.get("https://api.github.com/users/defunkt")
    body = r.json()
    headers = r.headers

    assert body["name"] == "Chris Wanstrath"
    assert r.status_code == 200
    assert headers["Server"] == "GitHub.com"


@pytest.mark.http
def test_status_code_request():
    r = requests.get("https://api.github.com/users/sergii_butenko")

    assert r.status_code == 404


@pytest.mark.skip
@pytest.mark.http
def test_current_user_repo():
    r = requests.get("https://api.github.com/users/lykhorovych")
    body = r.json()
    headers = r.headers

    assert r.status_code == 200
    assert body["login"] == "lykhorovych"
    assert body["url"] == "https://api.github.com/users/lykhorovych"
    assert headers["Server"] == "GitHub.com"


@pytest.mark.http
def test_github(github_api):
    print(github_api)
