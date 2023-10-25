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
    def test_check_user_sergii(self, database_api):
        user = database_api.get_user_address_by_name(name="Sergii")

        assert user[0][0] == "Maydan Nezalezhnosti 1"
        assert user[0][1] == "Kyiv"
        assert user[0][2] == "3127"
        assert user[0][3] == "Ukraine"

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

    @pytest.mark.new
    def test_check_types_field_in_products_table(self, database_api):
        user = database_api.get_user_address_by_name(name="Sergii")
        print(user)
        assert isinstance(user[0][0], str)
        assert isinstance(user[0][1], str)
        assert isinstance(user[0][2], str)
        assert isinstance(user[0][3], str)

    @pytest.mark.new
    def test_append_field_with_invalid_type_of_data(self, database_api):
        database_api.update_product_qnt_by_id(product_id=1, qnt="text")
        water_qnt = database_api.select_product_qnt_by_id(product_id=1)

        print(water_qnt)
        assert isinstance(water_qnt[0][0], int)
