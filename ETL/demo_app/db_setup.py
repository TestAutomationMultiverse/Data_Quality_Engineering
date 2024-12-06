import os
import psycopg2

SOURCE_DB_CONFIG = {
    "host": "source_db",
    "database": "old_db",
    "user": os.getenv("DB_USER", "user"),
    "password": os.getenv("DB_PASSWORD", "password"),
    "port": 5433,
}


TARGET_DB_CONFIG = {
    "host": "localhost",
    "database": "target_db",
    "user": "user",
    "password": "password",
    "port": 5432,
}

def create_table(connection, table_name):
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER,
        city VARCHAR(50)
    );
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
    connection.commit()

def insert_sample_data(connection, table_name):
    query = f"""
    INSERT INTO {table_name} (name, age, city) VALUES
    ('Alice', 30, 'New York'),
    ('Bob', 25, 'Los Angeles'),
    ('Charlie', 35, 'Chicago'),
    ('Diana', 28, 'San Francisco');
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
    connection.commit()

def setup_database(config, table_name):
    connection = psycopg2.connect(**config)
    create_table(connection, table_name)
    insert_sample_data(connection, table_name)
    connection.close()

if __name__ == "__main__":
    setup_database(SOURCE_DB_CONFIG, "source_table")
    setup_database(TARGET_DB_CONFIG, "target_table")  # Initially empty
