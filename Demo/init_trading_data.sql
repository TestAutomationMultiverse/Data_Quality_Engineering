-- Create the trades table
CREATE TABLE trades (
    trade_id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    timestamp TIMESTAMP,
    price DECIMAL(10, 2),
    quantity INT
);

-- Insert some sample trades
INSERT INTO trades (symbol, timestamp, price, quantity) VALUES
('AAPL', '2024-11-01 09:00:00', 145.25, 100),
('AAPL', '2024-11-01 09:15:00', 146.00, 150),
('AAPL', '2024-11-01 09:30:00', 144.80, 200),
('GOOG', '2024-11-01 09:00:00', 2765.50, 50),
('GOOG', '2024-11-01 09:30:00', 2775.00, 60),
('GOOG', '2024-11-01 10:00:00', 2755.00, 40),
('TSLA', '2024-11-01 09:00:00', 274.25, 120),
('TSLA', '2024-11-01 09:15:00', 275.00, 130),
('TSLA', '2024-11-01 09:30:00', 272.50, 160);
