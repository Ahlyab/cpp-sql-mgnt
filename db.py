import sqlite3


def create_db_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(database=db_name)
        print("SQLite Database connection successful")
    except sqlite3.Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except sqlite3.Error as err:
        print(f"Error: '{err}'")


connection = create_db_connection("users.db")
createDatabaseQuery = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
"""
execute_query(connection, createDatabaseQuery)
