import sqlite3
from decimal import Decimal
import pytest

class TestDataBase:
    @pytest.mark.database
    def test_database_connection(self, database_api):
        database_api.test_connection()

    @pytest.mark.database
    def test_check_all_users(self, database_api):
        users = database_api.get_all_users()

        print(users)

    @pytest.mark.database
    def test_check_all_products(self, database_api):
        products = database_api.get_all_products()

        print(products)

    @pytest.mark.database
    def test_check_user_sergii(self, database_api):
        user = database_api.get_user_address_by_name(name="Sergii")

        assert user[0][0] == "Maydan Nezalezhnosti 1"
        assert user[0][1] == "Kyiv"
        assert user[0][2] == "3127"
        assert user[0][3] == "Ukraine"

    @pytest.mark.database
    def test_check_user_sergii_negative(self, database_api):
        user = database_api.get_user_address_by_name(name='sergii')

        assert len(user) == 0

    @pytest.mark.database
    def test_get_full_address(self, database_api):
        user = database_api.get_user_address_by_name(name="Sergii")
        assert ", ".join(user[0]) == "Maydan Nezalezhnosti 1, Kyiv, 3127, Ukraine"

    @pytest.mark.database
    def test_product_qnt_update(self, database_api):
        database_api.update_product_qnt_by_id(product_id=1, qnt=25)
        water_qnt = database_api.select_product_qnt_by_id(product_id=1)

        assert water_qnt[0][0] == 25

    @pytest.mark.database
    def test_product_insert(self, database_api):
        database_api.insert_product(
            product_id=4, name="печиво", description="солодке", qnt=30
        )
        water_qnt = database_api.select_product_qnt_by_id(product_id=4)

        assert water_qnt[0][0] == 30

    @pytest.mark.database
    def test_product_delete(self, database_api):
        database_api.insert_product(
            product_id=99, name="тестові", description="дані", qnt=999
        )
        database_api.delete_product_by_id(product_id=99)
        qnt = database_api.select_product_qnt_by_id(product_id=99)

        assert len(qnt) == 0

    @pytest.mark.database
    def test_detailed_orders(self, database_api):
        orders = database_api.get_detailed_orders()
        print("Замовлення", orders)
        # Check quantity of orders equal to 1
        assert len(orders) == 1

        # Check structure of data
        assert orders[0][0] == 1
        assert orders[0][1] == "Sergii"
        assert orders[0][2] == "солодка вода"
        assert orders[0][3] == "з цукром"

    @pytest.mark.database
    def test_check_types_field_in_customers_table(self, database_api):
        user = database_api.get_user_address_by_name(name="Sergii")

        assert isinstance(user[0][0], str)
        assert isinstance(user[0][1], str)
        assert isinstance(user[0][2], str)
        assert isinstance(user[0][3], str)

    @pytest.mark.database
    def test_check_types_field_in_products_table(self, database_api):
        product = database_api.get_product_by_id(product_id=1)

        assert isinstance(product[0][0], int)
        assert isinstance(product[0][1], str)
        assert isinstance(product[0][2], str)
        assert isinstance(product[0][3], int)

    @pytest.mark.parametrize("quantity,error_message", [
        (Decimal("3.14"), "Error binding parameter 4: type 'decimal.Decimal' is not supported"),
        (complex(3, 14), "Error binding parameter 4: type 'complex' is not supported")
    ])
    @pytest.mark.database
    def test_product_insert_incorrect_quantity(self, database_api, quantity, error_message):
        try:
            database_api.insert_product(
            product_id=4, name="печиво", description="солодке", qnt=quantity
            )
        except sqlite3.ProgrammingError as err:
            assert err.args[0] == error_message
        except sqlite3.InterfaceError as err:
            assert err.args[0] == "Error binding parameter 3 - probably unsupported type."
        finally:
            product = database_api.select_product_by_id(product_id=4)
            assert product[0][3] == 30

    @pytest.mark.database
    def test_product_insert_incorrect_name(self, database_api):
        try:
            database_api.insert_product(
            product_id=4, name=list('печиво'), description="солодке", qnt=30
            )
        except sqlite3.ProgrammingError as err:
            assert err.args[0] == "Error binding parameter 2: type 'list' is not supported"
        except sqlite3.InterfaceError as err:
            assert err.args[0] == "Error binding parameter 1 - probably unsupported type."
        finally:
            product = database_api.select_product_by_id(product_id=4)
            assert product[0][1] == 'печиво'

    @pytest.mark.database
    def test_product_insert_incorrect_description(self, database_api):
        try:
            database_api.insert_product(
            product_id=4, name="печиво", description=list('солодке'), qnt=30
            )
        except sqlite3.ProgrammingError as err:
            assert err.args[0] == "Error binding parameter 3: type 'list' is not supported"
        except sqlite3.InterfaceError as err:
            assert err.args[0] == "Error binding parameter 2 - probably unsupported type."
        finally:
            product = database_api.select_product_by_id(product_id=4)
            assert product[0][2] == 'солодке'

    @pytest.mark.parametrize("quantity, error_message",
                             [
                             ([30,], "Error binding parameter 1: type 'list' is not supported"),
                             ((30, ), "Error binding parameter 1: type 'tuple' is not supported"),
                             ({30,}, "Error binding parameter 1: type 'set' is not supported"),
                             (Decimal("3.14"), "Error binding parameter 1: type 'decimal.Decimal' is not supported"),
                             (complex(3, 14), "Error binding parameter 1: type 'complex' is not supported")
                             ]
                             )
    @pytest.mark.database
    def test_update_quantity_negative(self, database_api, quantity, error_message):
        try:
            database_api.update_product_qnt_by_id(product_id=1, qnt=quantity)
        except sqlite3.ProgrammingError as err:
            assert err.args[0] == error_message
        except sqlite3.IntegrityError as err:
            assert err.args[0] == "Error binding parameter 0 - probably unsupported type."
        finally:
            water_qnt = database_api.select_product_qnt_by_id(product_id=1)

            assert water_qnt[0][0] == 25

    @pytest.mark.database
    def test_select_product_by_unknown_id(self, database_api):
        prd = database_api.select_product_qnt_by_id(product_id=999)

        assert len(prd) == 0

    @pytest.mark.database
    def test_correct_update_postal_code(self, database_api):
        database_api.update_customer_postalCode_by_name(name='Sergii', postal_code=3127)
        user = database_api.get_user_address_by_name(name='Sergii')

        assert user[0][2] == "3127"

    @pytest.mark.parametrize("postal_code,error_message",
                             [(Decimal("3.127"), "Error binding parameter 1: type 'decimal.Decimal' is not supported"),
                              (complex(3127), "Error binding parameter 1: type 'complex' is not supported")])
    @pytest.mark.database
    def test_update_postal_code_negative(self, database_api, postal_code, error_message):
        try:
            database_api.update_customer_postalCode_by_name(name='Sergii', postal_code=postal_code)
        except sqlite3.ProgrammingError as err:
            assert err.args[0] == error_message
        except sqlite3.IntegrityError as err:
            assert err.args[0] == "Error binding parameter 0 - probably unsupported type."
        finally:
            user = database_api.get_user_address_by_name(name='Sergii')
            assert user[0][2] == '3127'