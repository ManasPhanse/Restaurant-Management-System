use restaurant;

CREATE TABLE waiters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    waiter_name VARCHAR(255) NOT NULL,
    waiter_address VARCHAR(255) NOT NULL
);

CREATE TABLE tables (
    id INT AUTO_INCREMENT PRIMARY KEY,
    no_of_seats INT
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    order_type ENUM('drink', 'soup', 'appetizer', 'main course', 'dessert') NOT NULL,
    veg_nonveg ENUM('Vegetarian', 'Non-vegetarian') NOT NULL,
    quantity INT,
    price_per_quantity INT,
    table_id INT,
    waiter_id INT,
    FOREIGN KEY (table_id) REFERENCES tables(id),
    FOREIGN KEY (waiter_id) REFERENCES waiters(id)
);

CREATE TABLE drinks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    drink_type ENUM('Cocktail', 'Mocktail', 'Other Bevarages') NOT NULL,
    name VARCHAR(255) NOT NULL,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

CREATE TABLE soups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

CREATE TABLE appetizers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    appetizer_type ENUM('Chinese', 'Tandoor', 'Pakoras') NOT NULL,
    name VARCHAR(255) NOT NULL,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

CREATE TABLE main_courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    main_course_type ENUM('Chinese', 'Indian') NOT NULL,
    name VARCHAR(255) NOT NULL,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

CREATE TABLE desserts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dessert_type ENUM('Ice Cream', 'Cakes', 'Sweets') NOT NULL,
    name VARCHAR(255) NOT NULL,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);