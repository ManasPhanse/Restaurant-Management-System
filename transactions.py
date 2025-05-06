import mysql.connector
from getpass import getpass
from tabulate import tabulate

# Function to create a connection to the "restaurant" database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=getpass("Enter Password: "),
        database="restaurant"
    )

# Display the main menu options for restaurant order management
def display_menu():
    print("\n===== Restaurant Order Management System =====")
    print("1. Place an order")
    print("2. Modify an order")
    print("3. Delete an order")
    print("4. View orders")
    print("5. Exit")

# Route the user's choice to the corresponding function
def handle_choice(choice, conn):
    if choice == "1":
        place_order(conn)
    elif choice == "2":
        modify_order(conn)
    elif choice == "3":
        delete_order(conn)
    elif choice == "4":
        view_orders(conn)
    elif choice == "5":
        print("Exiting...")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

# Place an order by inserting a record into orders and then into the appropriate detail table
def place_order(conn):
    try:
        cursor = conn.cursor()
        print("\nEnter Order Details:")
        order_type = input("Order type (drink, soup, appetizer, main course, dessert): ").strip().lower()
        if order_type not in ['drink', 'soup', 'appetizer', 'main course', 'dessert']:
            print("Invalid order type!")
            return

        veg_nonveg = input("Vegetarian or Non-vegetarian: ").strip().title()
        quantity = int(input("Enter quantity: "))
        price_per_quantity = int(input("Enter price per quantity: "))
        table_id = int(input("Enter table ID: "))
        waiter_id = int(input("Enter waiter ID: "))

        order_query = """
            INSERT INTO orders (order_type, veg_nonveg, quantity, price_per_quantity, table_id, waiter_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        order_data = (order_type, veg_nonveg, quantity, price_per_quantity, table_id, waiter_id)
        cursor.execute(order_query, order_data)
        order_id = cursor.lastrowid  # Capture the generated order id

        # Now insert the order's specific details based on its type
        if order_type == "drink":
            drink_type = input("Enter drink type (Cocktail, Mocktail, Other Bevarages): ").strip()
            drink_name = input("Enter drink name: ").strip()
            detail_query = """
                INSERT INTO drinks (drink_type, name, order_id)
                VALUES (%s, %s, %s)
            """
            detail_data = (drink_type, drink_name, order_id)
        elif order_type == "soup":
            soup_name = input("Enter soup name: ").strip()
            detail_query = """
                INSERT INTO soups (name, order_id)
                VALUES (%s, %s)
            """
            detail_data = (soup_name, order_id)
        elif order_type == "appetizer":
            appetizer_type = input("Enter appetizer type (Chinese, Tandoor, Pakoras): ").strip()
            appetizer_name = input("Enter appetizer name: ").strip()
            detail_query = """
                INSERT INTO appetizers (appetizer_type, name, order_id)
                VALUES (%s, %s, %s)
            """
            detail_data = (appetizer_type, appetizer_name, order_id)
        elif order_type == "main course":
            main_course_type = input("Enter main course type (Chinese, Indian): ").strip()
            main_course_name = input("Enter main course name: ").strip()
            detail_query = """
                INSERT INTO main_courses (main_course_type, name, order_id)
                VALUES (%s, %s, %s)
            """
            detail_data = (main_course_type, main_course_name, order_id)
        elif order_type == "dessert":
            dessert_type = input("Enter dessert type (Ice Cream, Cakes, Sweets): ").strip()
            dessert_name = input("Enter dessert name: ").strip()
            detail_query = """
                INSERT INTO desserts (dessert_type, name, order_id)
                VALUES (%s, %s, %s)
            """
            detail_data = (dessert_type, dessert_name, order_id)
        else:
            print("Unknown order type!")
            return

        cursor.execute(detail_query, detail_data)
        conn.commit()
        print("Order placed successfully with Order ID:", order_id)
    except Exception as e:
        print("Error while placing order:", e)
    finally:
        cursor.close()

# Modify an existing order and its corresponding detail record
def modify_order(conn):
    try:
        cursor = conn.cursor()
        order_id = int(input("\nEnter the Order ID to modify: "))
        
        # Retrieve existing order details
        fetch_query = "SELECT order_type, veg_nonveg, quantity, price_per_quantity, table_id, waiter_id FROM orders WHERE id = %s"
        cursor.execute(fetch_query, (order_id,))
        order = cursor.fetchone()
        
        if not order:
            print("Order not found!")
            return
        
        order_type, veg_nonveg_old, quantity_old, price_old, table_id_old, waiter_id_old = order
        print("\nCurrent Order Details:")
        print("Order Type   :", order_type)
        print("Veg/Non-veg  :", veg_nonveg_old)
        print("Quantity     :", quantity_old)
        print("Price        :", price_old)
        print("Table ID     :", table_id_old)
        print("Waiter ID    :", waiter_id_old)
        
        # Prompt for new values, allowing blanks to retain current values
        new_veg_nonveg = input("Enter new Veg/Non-vegetarian (leave blank to keep current): ").strip().title() or veg_nonveg_old
        new_quantity = input("Enter new Quantity (leave blank to keep current): ").strip()
        new_price = input("Enter new Price per Quantity (leave blank to keep current): ").strip()
        new_table_id = input("Enter new Table ID (leave blank to keep current): ").strip()
        new_waiter_id = input("Enter new Waiter ID (leave blank to keep current): ").strip()
        
        new_quantity = int(new_quantity) if new_quantity else quantity_old
        new_price = float(new_price) if new_price else price_old
        new_table_id = int(new_table_id) if new_table_id else table_id_old
        new_waiter_id = int(new_waiter_id) if new_waiter_id else waiter_id_old
        
        update_query = """
            UPDATE orders
            SET veg_nonveg = %s, quantity = %s, price_per_quantity = %s, table_id = %s, waiter_id = %s
            WHERE id = %s
        """
        cursor.execute(update_query, (new_veg_nonveg, new_quantity, new_price, new_table_id, new_waiter_id, order_id))
        
        # Modify the detail entry in the corresponding detail table based on the order type
        if order_type == "drink":
            cursor.execute("SELECT drink_type, name FROM drinks WHERE order_id = %s", (order_id,))
            detail = cursor.fetchone()
            if detail:
                current_drink_type, current_drink_name = detail
                new_drink_type = input(f"Enter new drink type (current: {current_drink_type}, leave blank to keep): ").strip() or current_drink_type
                new_drink_name = input(f"Enter new drink name (current: {current_drink_name}, leave blank to keep): ").strip() or current_drink_name
                update_detail_query = """
                    UPDATE drinks
                    SET drink_type = %s, name = %s
                    WHERE order_id = %s
                """
                cursor.execute(update_detail_query, (new_drink_type, new_drink_name, order_id))
        elif order_type == "soup":
            cursor.execute("SELECT name FROM soups WHERE order_id = %s", (order_id,))
            detail = cursor.fetchone()
            if detail:
                current_name = detail[0]
                new_name = input(f"Enter new soup name (current: {current_name}, leave blank to keep): ").strip() or current_name
                update_detail_query = "UPDATE soups SET name = %s WHERE order_id = %s"
                cursor.execute(update_detail_query, (new_name, order_id))
        elif order_type == "appetizer":
            cursor.execute("SELECT appetizer_type, name FROM appetizers WHERE order_id = %s", (order_id,))
            detail = cursor.fetchone()
            if detail:
                current_type, current_name = detail
                new_type = input(f"Enter new appetizer type (current: {current_type}, leave blank to keep): ").strip() or current_type
                new_name = input(f"Enter new appetizer name (current: {current_name}, leave blank to keep): ").strip() or current_name
                update_detail_query = """
                    UPDATE appetizers
                    SET appetizer_type = %s, name = %s
                    WHERE order_id = %s
                """
                cursor.execute(update_detail_query, (new_type, new_name, order_id))
        elif order_type == "main course":
            cursor.execute("SELECT main_course_type, name FROM main_courses WHERE order_id = %s", (order_id,))
            detail = cursor.fetchone()
            if detail:
                current_type, current_name = detail
                new_type = input(f"Enter new main course type (current: {current_type}, leave blank to keep): ").strip() or current_type
                new_name = input(f"Enter new main course name (current: {current_name}, leave blank to keep): ").strip() or current_name
                update_detail_query = """
                    UPDATE main_courses
                    SET main_course_type = %s, name = %s
                    WHERE order_id = %s
                """
                cursor.execute(update_detail_query, (new_type, new_name, order_id))
        elif order_type == "dessert":
            cursor.execute("SELECT dessert_type, name FROM desserts WHERE order_id = %s", (order_id,))
            detail = cursor.fetchone()
            if detail:
                current_type, current_name = detail
                new_type = input(f"Enter new dessert type (current: {current_type}, leave blank to keep): ").strip() or current_type
                new_name = input(f"Enter new dessert name (current: {current_name}, leave blank to keep): ").strip() or current_name
                update_detail_query = """
                    UPDATE desserts
                    SET dessert_type = %s, name = %s
                    WHERE order_id = %s
                """
                cursor.execute(update_detail_query, (new_type, new_name, order_id))
        
        conn.commit()
        print("Order modified successfully!")
    except Exception as e:
        print("Error while modifying order:", e)
    finally:
        cursor.close()

# Delete an order, including its detail row from the appropriate table
def delete_order(conn):
    try:
        cursor = conn.cursor()
        order_id = int(input("\nEnter the Order ID to delete: "))
        
        # Determine which detail table must be cleared based on order type
        cursor.execute("SELECT order_type FROM orders WHERE id = %s", (order_id,))
        result = cursor.fetchone()
        if not result:
            print("Order not found!")
            return
        
        order_type = result[0]
        if order_type == "drink":
            cursor.execute("DELETE FROM drinks WHERE order_id = %s", (order_id,))
        elif order_type == "soup":
            cursor.execute("DELETE FROM soups WHERE order_id = %s", (order_id,))
        elif order_type == "appetizer":
            cursor.execute("DELETE FROM appetizers WHERE order_id = %s", (order_id,))
        elif order_type == "main course":
            cursor.execute("DELETE FROM main_courses WHERE order_id = %s", (order_id,))
        elif order_type == "dessert":
            cursor.execute("DELETE FROM desserts WHERE order_id = %s", (order_id,))
        
        # Now delete the order record
        cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
        conn.commit()
        print("Order deleted successfully!")
    except Exception as e:
        print("Error while deleting order:", e)
    finally:
        cursor.close()

# View orders from the corresponding detail table
def view_orders(conn):
    try:
        cursor = conn.cursor()
        print("\n===== View Orders =====")
        print("1. Sort by Order ID")
        print("2. Sort by Order Date")
        print("3. Sort by Order Type")
        print("4. Back to Main Menu")
        
        sort_choice = input("Enter your sort choice (1-4): ")
        if sort_choice == "1":
            order_by = "o.id"
        elif sort_choice == "2":
            order_by = "o.order_date"
        elif sort_choice == "3":
            order_by = "o.order_type"
        elif sort_choice == "4":
            return
        else:
            print("Invalid choice. Returning to main menu.")
            return
        
        # This query joins the orders table with the respective detail table based on order type,
        # calculates the price per quantity, and selects the ordered dish (dish name).
        query = f"""
            SELECT o.id,
                   o.order_date,
                   o.order_type,
                   o.veg_nonveg,
                   o.quantity,
                   o.price_per_quantity,
                   (o.price_per_quantity * o.quantity) AS price,
                   CASE
                       WHEN o.order_type = 'drink' THEN d.name
                       WHEN o.order_type = 'soup' THEN s.name
                       WHEN o.order_type = 'appetizer' THEN a.name
                       WHEN o.order_type = 'main course' THEN m.name
                       WHEN o.order_type = 'dessert' THEN ds.name
                       ELSE 'N/A'
                   END AS ordered_dish,
                   o.table_id,
                   -- t.no_of_seats AS `Table Size`,
                   -- w.waiter_name AS `Waiter`,
                   o.waiter_id
            FROM orders o
            LEFT JOIN drinks d ON o.id = d.order_id AND o.order_type = 'drink'
            LEFT JOIN soups s ON o.id = s.order_id AND o.order_type = 'soup'
            LEFT JOIN appetizers a ON o.id = a.order_id AND o.order_type = 'appetizer'
            LEFT JOIN main_courses m ON o.id = m.order_id AND o.order_type = 'main course'
            LEFT JOIN desserts ds ON o.id = ds.order_id AND o.order_type = 'dessert'
            -- LEFT JOIN waiters w ON o.waiter_id = w.id
            -- LEFT JOIN tables t ON o.table_id = t.id
            ORDER BY {order_by}
        """
        cursor.execute(query)
        orders = cursor.fetchall()
        
        if not orders:
            print("No orders found!")
        else:
            headers = [
                "ID",
                "Order Date",
                "Order Type",
                "Veg/Non-Veg",
                "Quantity",
                "Price",
                "Price per Qty",
                "Ordered Dish",
                "Table ID",
                "Waiter ID"
            ]
            print("\n" + tabulate(orders, headers, tablefmt="pretty"))
    except Exception as e:
        print("Error retrieving orders:", e)
    finally:
        cursor.close()

# Main program loop
def main():
    conn = create_connection()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if not handle_choice(choice, conn):
            break
    conn.close()

if __name__ == "__main__":
    main()
