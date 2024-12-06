from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database configurations from environment variables
SOURCE_DB_CONFIG = {
    "host": "host.docker.internal",  # This should match the service/container name
    "database": "old_db",
    "user": "user",
    "password": "password",
    "port": 5433,
}

TARGET_DB_CONFIG = {
    "host": "host.docker.internal",
    "database": "new_db",
    "user": "user",
    "password": "password",
    "port": 5434,  # Target DB uses host port 5434
}

def migrate_users():
    query = """
    SELECT id, name, age, city, created_at FROM source_table;
    """
    connection = psycopg2.connect(**SOURCE_DB_CONFIG)
    with connection.cursor() as cursor:
        cursor.execute(query)
        users = cursor.fetchall()
    connection.close()

    # Transform data
    transformed_users = [
        (
            user[0],  # user_id
            user[1],  # full_name
            '<30' if user[2] < 30 else '30-40' if user[2] <= 40 else '>40',  # age_group
            user[3],  # city
            user[4],  # registered_date
        )
        for user in users
    ]

    # Insert transformed data
    connection = psycopg2.connect(**TARGET_DB_CONFIG)
    with connection.cursor() as cursor:
        for user in transformed_users:
            cursor.execute(
                "INSERT INTO target_users (user_id, full_name, age_group, city, registered_date) VALUES (%s, %s, %s, %s, %s);",
                user,
            )
    connection.commit()
    connection.close()

def migrate_orders():
    query = """
    SELECT order_id, user_id, order_total, order_date FROM source_orders;
    """
    connection = psycopg2.connect(**SOURCE_DB_CONFIG)
    with connection.cursor() as cursor:
        cursor.execute(query)
        orders = cursor.fetchall()
    connection.close()

    # Insert orders into target
    connection = psycopg2.connect(**TARGET_DB_CONFIG)
    with connection.cursor() as cursor:
        for order in orders:
            cursor.execute(
                "INSERT INTO target_orders (order_id, user_id, order_total, order_date) VALUES (%s, %s, %s, %s);",
                order,
            )
    connection.commit()
    connection.close()

def migrate_cleaned_data():
    query = """
    SELECT record_id, full_name, age, location FROM source_unnormalized;
    """
    connection = psycopg2.connect(**SOURCE_DB_CONFIG)
    with connection.cursor() as cursor:
        cursor.execute(query)
        records = cursor.fetchall()
    connection.close()

    # Clean and transform data
    cleaned_data = [
        (
            record[0],  # record_id
            record[1].split(' ')[0],  # name (first name)
            int(record[2]),  # age (as integer)
            record[3],  # city
        )
        for record in records
    ]

    # Insert cleaned data
    connection = psycopg2.connect(**TARGET_DB_CONFIG)
    with connection.cursor() as cursor:
        for record in cleaned_data:
            cursor.execute(
                "INSERT INTO target_cleaned_data (record_id, name, age, city) VALUES (%s, %s, %s, %s);",
                record,
            )
    connection.commit()
    connection.close()

@app.route('/migrate-users', methods=['POST'])
def migrate_users_endpoint():
    migrate_users()
    return jsonify({"message": "Users migrated successfully."})

@app.route('/migrate-orders', methods=['POST'])
def migrate_orders_endpoint():
    migrate_orders()
    return jsonify({"message": "Orders migrated successfully."})

@app.route('/migrate-cleaned-data', methods=['POST'])
def migrate_cleaned_data_endpoint():
    migrate_cleaned_data()
    return jsonify({"message": "Cleaned data migrated successfully."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
