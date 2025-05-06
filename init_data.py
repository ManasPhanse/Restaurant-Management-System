import mysql.connector
from getpass import getpass

# Connect to MySQL database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=getpass("Enter Password: "),
        database="restaurant"
    )

def insert_initial_data():
    conn = create_connection()
    cursor = conn.cursor()

    # Insert waiters
    waiter_insert_query = """
        INSERT INTO waiters (waiter_name, waiter_address)
        VALUES (%s, %s)
    """
    waiters = [
        ('John Doe', '123 Main St'),
        ('Alice Smith', '456 Elm Street'),
        ('Bob Brown', '789 Pine Ave')
    ]
    cursor.executemany(waiter_insert_query, waiters)

    # Insert tables (restaurant seating)
    table_insert_query = """
        INSERT INTO tables (no_of_seats)
        VALUES (%s)
    """
    tables_data = [
        (4,),
        (2,),
        (6,),
        (8,)
    ]
    cursor.executemany(table_insert_query, tables_data)

    # Insert a drink order and its detail in drinks table
    order_insert_query = """
        INSERT INTO orders (order_type, veg_nonveg, quantity, price_per_quantity, table_id, waiter_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    drink_order_data = ('drink', 'Vegetarian', 2, 150, 1, 1)
    cursor.execute(order_insert_query, drink_order_data)
    drink_order_id = cursor.lastrowid  # Capture auto-generated order id

    drink_detail_query = """
        INSERT INTO drinks (drink_type, name, order_id)
        VALUES (%s, %s, %s)
    """
    drink_detail_data = ('Cocktail', 'Mojito', drink_order_id)
    cursor.execute(drink_detail_query, drink_detail_data)

    # Insert a soup order and its detail in soups table
    soup_order_data = ('soup', 'Non-vegetarian', 1, 200, 2, 2)
    cursor.execute(order_insert_query, soup_order_data)
    soup_order_id = cursor.lastrowid

    soup_detail_query = """
        INSERT INTO soups (name, order_id)
        VALUES (%s, %s)
    """
    soup_detail_data = ('Chicken Soup', soup_order_id)
    cursor.execute(soup_detail_query, soup_detail_data)

    # Insert an appetizer order and its detail in appetizers table
    appetizer_order_data = ('appetizer', 'Vegetarian', 3, 100, 3, 3)
    cursor.execute(order_insert_query, appetizer_order_data)
    appetizer_order_id = cursor.lastrowid

    appetizer_detail_query = """
        INSERT INTO appetizers (appetizer_type, name, order_id)
        VALUES (%s, %s, %s)
    """
    appetizer_detail_data = ('Pakoras', 'Onion Pakoras', appetizer_order_id)
    cursor.execute(appetizer_detail_query, appetizer_detail_data)

    # Insert a main course order and its detail in main_courses table
    main_course_order_data = ('main course', 'Non-vegetarian', 1, 500, 1, 2)
    cursor.execute(order_insert_query, main_course_order_data)
    main_course_order_id = cursor.lastrowid

    main_course_detail_query = """
        INSERT INTO main_courses (main_course_type, name, order_id)
        VALUES (%s, %s, %s)
    """
    main_course_detail_data = ('Indian', 'Butter Chicken', main_course_order_id)
    cursor.execute(main_course_detail_query, main_course_detail_data)

    # Insert a dessert order and its detail in desserts table
    dessert_order_data = ('dessert', 'Vegetarian', 2, 250, 2, 1)
    cursor.execute(order_insert_query, dessert_order_data)
    dessert_order_id = cursor.lastrowid

    dessert_detail_query = """
        INSERT INTO desserts (dessert_type, name, order_id)
        VALUES (%s, %s, %s)
    """
    dessert_detail_data = ('Ice Cream', 'Vanilla Ice Cream', dessert_order_id)
    cursor.execute(dessert_detail_query, dessert_detail_data)

    # Commit all changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Initial data inserted successfully!")

if __name__ == '__main__':
    insert_initial_data()
