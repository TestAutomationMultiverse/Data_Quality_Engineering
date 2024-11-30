import os
import psycopg2
import pandas as pd
from datetime import datetime

# Database connection settings
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=db_host, user=db_user, password=db_password, dbname=db_name
)

# Extract data: Get trades from the "trades" table
query = "SELECT * FROM trades"
df = pd.read_sql(query, conn)

# Transform data

# Add a new column for the date only (ignoring time)
df['date'] = df['timestamp'].dt.date

# Group by date and symbol, then calculate average price and total volume traded
daily_summary = df.groupby(['date', 'symbol']).agg(
    average_price=('price', 'mean'),
    total_volume_traded=('quantity', 'sum')
).reset_index()

# Calculate daily returns (percentage change) for each symbol
daily_summary['daily_return'] = daily_summary.groupby('symbol')['average_price'].pct_change() * 100

# Load transformed data into the "daily_summary" table
daily_summary.to_sql('daily_summary', conn, if_exists='replace', index=False)

# Test: Verify that the transformation is correct
test_query = "SELECT * FROM daily_summary"
test_df = pd.read_sql(test_query, conn)

# Validation: Check if daily returns were calculated correctly
for symbol in test_df['symbol'].unique():
    symbol_data = test_df[test_df['symbol'] == symbol]
    if len(symbol_data) > 1:
        # Ensure daily returns are not NaN for multiple rows
        assert not symbol_data['daily_return'].isna().any(), f"Daily returns missing for {symbol}"

# Close the connection
conn.close()

print("ETL process completed and data transformation validated successfully.")
