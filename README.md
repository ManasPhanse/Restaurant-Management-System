# Restaurant-Management-System
A simple Restaurant Order Management System based on Python and MySQL

1. tables.sql creates tables tables
2. DB can created using drop_n_replace_schema.py file
3. Tables can also be generated using new_tables.py
4. init_data.py can be used insert dummy data
5. transactions.py is the interface program

## Running Instance (Using VS Code)

PS C:\Users\Manas> & C:/Users/Manas/AppData/Local/Programs/Python/Python313/python.exe c:/Users/Manas/Desktop/order_mgmt/transactions.py
Enter Password: 

===== Restaurant Order Management System =====
1. Place an order
2. Modify an order
3. Delete an order
4. View orders
5. Exit
Enter your choice: 4

===== View Orders =====
1. Sort by Order ID
2. Sort by Order Date
3. Sort by Order Type
4. Back to Main Menu
Enter your sort choice (1-4): 1

+----+---------------------+-------------+----------------+----------+-------+---------------+---------------------+----------+-----------+ -m
| ID |     Order Date      | Order Type  |  Veg/Non-Veg   | Quantity | Price | Price per Qty |    Ordered Dish     | Table ID | Waiter ID | -m
+----+---------------------+-------------+----------------+----------+-------+---------------+---------------------+----------+-----------+ -m
| 1  | 2025-05-06 19:45:45 |    drink    |   Vegetarian   |    2     |  150  |      300      |       Mojito        |    1     |     1     | -m
| 2  | 2025-05-06 19:45:45 |    soup     | Non-vegetarian |    1     |  200  |      200      |    Chicken Soup     |    2     |     2     | -m
| 3  | 2025-05-06 19:45:45 |  appetizer  |   Vegetarian   |    3     |  100  |      300      |    Onion Pakoras    |    3     |     3     | -m
| 4  | 2025-05-06 19:45:45 | main course | Non-vegetarian |    1     |  500  |      500      |   Butter Chicken    |    1     |     2     | -m
| 5  | 2025-05-06 19:45:45 |   dessert   |   Vegetarian   |    2     |  250  |      500      |  Vanilla Ice Cream  |    2     |     1     | -m
| 8  | 2025-05-06 20:30:19 | main course |   Vegetarian   |    1     |  200  |      200      | Paneer Tikka Masala |    2     |     3     | -m
+----+---------------------+-------------+----------------+----------+-------+---------------+---------------------+----------+-----------+ -m

===== Restaurant Order Management System =====
1. Place an order
2. Modify an order
3. Delete an order
4. View orders
5. Exit
Enter your choice: 1

Enter Order Details:
Order type (drink, soup, appetizer, main course, dessert): drink
Vegetarian or Non-vegetarian: Vegetarian
Enter quantity: 1
Enter price per quantity: 100
Enter table ID: 1
Enter waiter ID: 1
Enter drink type (Cocktail, Mocktail, Other Bevarages): Mocktail
Enter drink name: Ginger Ale
Order placed successfully with Order ID: 9

===== Restaurant Order Management System =====
1. Place an order
2. Modify an order
3. Delete an order
4. View orders
5. Exit
Enter your choice: 2

Enter the Order ID to modify: 9

Current Order Details:
Order Type   : drink
Veg/Non-veg  : Vegetarian
Quantity     : 1
Price        : 100
Table ID     : 1
Waiter ID    : 1
Enter new Veg/Non-vegetarian (leave blank to keep current):
Enter new Quantity (leave blank to keep current): 2
Enter new Price per Quantity (leave blank to keep current): 
Enter new Table ID (leave blank to keep current): 
Enter new Waiter ID (leave blank to keep current): 
Enter new drink type (current: Mocktail, leave blank to keep): Cocktail
Enter new drink name (current: Ginger Ale, leave blank to keep): Gin+Ginger Ale
Order modified successfully!

===== Restaurant Order Management System =====
1. Place an order
2. Modify an order
3. Delete an order
4. View orders
5. Exit
Enter your choice: 3

Enter the Order ID to delete: 9
Order deleted successfully!

===== Restaurant Order Management System =====
1. Place an order
2. Modify an order
3. Delete an order
4. View orders
5. Exit
Enter your choice: 4

===== View Orders =====
1. Sort by Order ID
2. Sort by Order Date
3. Sort by Order Type
4. Back to Main Menu
Enter your sort choice (1-4): 1

+----+---------------------+-------------+----------------+----------+-------+---------------+---------------------+----------+-----------+
| ID |     Order Date      | Order Type  |  Veg/Non-Veg   | Quantity | Price | Price per Qty |    Ordered Dish     | Table ID | Waiter ID |
+----+---------------------+-------------+----------------+----------+-------+---------------+---------------------+----------+-----------+
| 1  | 2025-05-06 19:45:45 |    drink    |   Vegetarian   |    2     |  150  |      300      |       Mojito        |    1     |     1     |
| 2  | 2025-05-06 19:45:45 |    soup     | Non-vegetarian |    1     |  200  |      200      |    Chicken Soup     |    2     |     2     |
| 3  | 2025-05-06 19:45:45 |  appetizer  |   Vegetarian   |    3     |  100  |      300      |    Onion Pakoras    |    3     |     3     |
| 4  | 2025-05-06 19:45:45 | main course | Non-vegetarian |    1     |  500  |      500      |   Butter Chicken    |    1     |     2     |
| 5  | 2025-05-06 19:45:45 |   dessert   |   Vegetarian   |    2     |  250  |      500      |  Vanilla Ice Cream  |    2     |     1     |
| 8  | 2025-05-06 20:30:19 | main course |   Vegetarian   |    1     |  200  |      200      | Paneer Tikka Masala |    2     |     3     |
+----+---------------------+-------------+----------------+----------+-------+---------------+---------------------+----------+-----------+

===== Restaurant Order Management System =====
1. Place an order
2. Modify an order
3. Delete an order
4. View orders
5. Exit
Enter your choice: 5
Exiting...
PS C:\Users\Manas>
