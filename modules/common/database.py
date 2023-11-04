import sqlite3
from config.config import BASE_DIR
class DataBase:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(
            BASE_DIR / 'become_qa_auto.db'
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite DataBase Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"""
        SELECT address, city, postalCode, country
        FROM customers
        WHERE name = '{name}'"""
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_all_products(self):
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_product_by_id(self, product_id: int):
        query = f"SELECT * FROM products WHERE id = {product_id}"

        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id: int, qnt: int):
        query = f"""
        UPDATE products
        SET quantity = ?
        WHERE id = {product_id}"""
        self.cursor.execute(query, (qnt, ))
        self.connection.commit()
    def update_customer_postalCode_by_name(self, name: str, postal_code: str):
        query = f"UPDATE customers SET postalCode = ? WHERE name = '{name}'"
        self.cursor.execute(query, (postal_code, ))
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"""
        SELECT quantity FROM products WHERE id = {product_id}"""
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def select_product_by_id(self, product_id):
        query = f"SELECT * FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    def insert_product(self, product_id: int, name: str, description: str, qnt: int):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity)\
                VALUES (?, ?, ?, ?);"

        self.cursor.execute(query, (product_id, name, description, qnt))
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"""
        DELETE FROM products
        WHERE id = {product_id};"""
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = """
        SELECT orders.id, customers.name, products.name, products.description, orders.order_date
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
        JOIN products ON orders.product_id = products.id;
        """
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def close(self):
        self.connection.close()
