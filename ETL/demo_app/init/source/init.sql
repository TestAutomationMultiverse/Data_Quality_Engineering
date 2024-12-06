CREATE TABLE IF NOT EXISTS source_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    city VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO source_table (name, age, city) VALUES
('Alice', 30, 'New York'),
('Bob', 25, 'Los Angeles'),
('Charlie', 35, 'Chicago'),
('Diana', 28, 'San Francisco'),
('Eve', 40, 'Boston');

CREATE TABLE IF NOT EXISTS source_orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER,
    order_total DECIMAL(10, 2),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES source_table (id)
);

INSERT INTO source_orders (user_id, order_total, order_date) VALUES
(1, 100.50, '2023-11-01 10:00:00'),
(2, 200.75, '2023-11-02 15:30:00'),
(1, 50.00, '2023-11-03 18:45:00'),
(3, 300.00, '2023-11-04 12:15:00'),
(4, 150.25, '2023-11-05 09:10:00');

CREATE TABLE IF NOT EXISTS source_unnormalized (
    record_id SERIAL PRIMARY KEY,
    full_name VARCHAR(150),
    age VARCHAR(10),
    location VARCHAR(100)
);

INSERT INTO source_unnormalized (full_name, age, location) VALUES
('Alice Johnson', '30', 'New York'),
('Bob Smith', '25', 'Los Angeles'),
('Charlie Brown', '35', 'Chicago'),
('Diana Ross', '28', 'San Francisco'),
('Eve Adams', '40', 'Boston');
