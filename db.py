import sqlite3


def createDbConnection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(database=db_name)
        print("SQLite Database connection successful")
    except sqlite3.Error as err:
        print(f"Error: '{err}'")

    return connection


connection = createDbConnection("users.db")


def executeQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        return True
    except sqlite3.Error as err:
        print(f"Error: '{err}'")
        return False


def checkIfUserExists(username):
    query = f"SELECT * FROM users WHERE username='{username}'"
    cursor = connection.cursor()
    cursor.execute(query)
    if cursor.fetchone():
        return True
    return False


def createUser(username, password):
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    executeQuery(connection, query)


def clearDb():
    """this will permanently delete the database, use with caution"""

    query = "DELETE FROM users"
    executeQuery(connection, query)
    query = "DELETE FROM sqlite_sequence WHERE name='users'"
    executeQuery(connection, query)
