import pytest
from modules.common.database import DataBase


@pytest.mark.database
def test_database_connection():
    db = DataBase()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = DataBase()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = DataBase()
    user = db.get_user_address_by_name(name="Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = DataBase()
    db.update_product_qnt_by_id(product_id=1, qnt=25)
    water_qnt = db.select_product_qnt_by_id(product_id=1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = DataBase()
    db.insert_product(product_id=4, name="печиво", description="солодке", qnt=30)
    water_qnt = db.select_product_qnt_by_id(product_id=4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = DataBase()
    db.insert_product(product_id=99, name="тестові", description="дані", qnt=999)
    db.delete_product_by_id(product_id=99)
    qnt = db.select_product_qnt_by_id(product_id=99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = DataBase()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"
