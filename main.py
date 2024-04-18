import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_product(connection, product):
    try:
        sql = '''INSERT INTO products 
                (product_title, price, quantity)
                VALUES (?, ?, ?)
                '''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_products_price(connection, product):
    try:
        sql = '''UPDATE products SET price = ?
        WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_products_quantity(connection, product):
    try:
        sql = '''UPDATE products SET quantity = ?
        WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_products(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_quantity(connection, quantity_limit):
    try:
        sql = '''SELECT * FROM products WHERE quantity >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (quantity_limit,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def find_name_products(connection, name_product):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (name_product,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL, 
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
    )
'''

my_connection = create_connection('hw.db')
if my_connection:
    print('Connected successfully!!!')
    # create_table(my_connection, sql_create_products_table)
    # insert_product(my_connection, ('Хозяйственное Мыло', 100, 5))
    # insert_product(my_connection, ('Детское Мыло', 150, 10))
    # insert_product(my_connection, ('Хлеб', 40, 20))
    # insert_product(my_connection, ('Кока-кола', 55, 60))
    # insert_product(my_connection, ('Мороженое Эскимо', 43, 22))
    # insert_product(my_connection, ('Мороженое Пламбир', 55, 18))
    # insert_product(my_connection, ('Мороженое Стаканчик', 25, 40))
    # insert_product(my_connection, ('Молоко', 50, 30))
    # insert_product(my_connection, ('Шампунь', 200, 3))
    # insert_product(my_connection, ('Зубная Паста', 50, 2))
    # insert_product(my_connection, ('Мыло для Рук', 80, 4))
    # insert_product(my_connection, ('Кофе', 100, 8))
    # insert_product(my_connection, ('Яйца', 20, 30))
    # insert_product(my_connection, ('Печенье', 45, 17))
    # insert_product(my_connection, ('Масло', 80, 10))
    # update_products_price(my_connection, (20, 8))
    # update_products_quantity(my_connection, (5,11))
    # delete_products(my_connection, 2)
    # select_all_products(my_connection)
    # select_products_quantity(my_connection, 5)
    # find_name_products(my_connection, ('%Мыло%'))
    my_connection.close()