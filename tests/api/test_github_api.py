import pytest
from icecream.icecream import ic
from pprint import pprint


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")

    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")

    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")

    assert r["total_count"] == 50
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")

    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")

    assert r["total_count"] != 0


@pytest.mark.api
def test_get_emojis(github_api):
    status_code, r = github_api.get_emojis()

    assert (
        status_code == 200
    ), f"The expected status code is 200, but {status_code} was received."
    assert isinstance(
        r, dict
    ), "The expected response is a dict, but a different one was received."


@pytest.mark.api
def test_list_repo_commits_exists(github_api):
    status_code, url, r = github_api.get_list_repo_commits("defunkt", "ace")

    assert (
        status_code == 200
    ), f"The expected status code is 200, but {status_code} was received."
    assert isinstance(
        r, list
    ), "The expected response is a list of commits, but a different outcome was received."
    assert (
        url in r[0]["url"]
    ), f"Expected that {url=} to be part of URL commits='{r[0]['url']}'"


@pytest.mark.api
def test_list_repo_commits_cannot_be_found(github_api):
    status_code, _, r = github_api.get_list_repo_commits(
        "butenkosergii", "sergiibutenko_repo_non_exist"
    )

    assert (
        status_code == 404
    ), f"The expected status code is 404, but {status_code} was received."
    assert (
        r["message"] == "Not Found"
    ), "The expected message is 'Not Found', but a different one was received."


@pytest.mark.api
def test_list_repo_languages(github_api):
    status_code, r = github_api.get_list_repo_languages("defunkt", "ace")

    assert (
        status_code == 200
    ), f"The expected status code is 200, but {status_code} was received."
    assert isinstance(
        r, dict
    ), f"The expected response is a dict with languages, but a different one was received."
    assert "Python" in r, "Expected to find Python in response"
