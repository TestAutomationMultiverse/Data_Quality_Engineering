import psycopg2
import pandas as pd

def connect_to_database(config):
    return psycopg2.connect(
        host=config['host'],
        database=config['database'],
        user=config['user'],
        password=config['password'],
        port=config['port']
    )

def fetch_data(query, connection):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
