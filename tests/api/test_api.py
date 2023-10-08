import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ""
    assert user.name == ""


@pytest.mark.change
def test_remove_second_name(user):
    user.second_name = ""
    assert user.second_name == ""


@pytest.mark.check
def test_name(user):
    assert user.name == "Oleh"


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Lykhorovych"
