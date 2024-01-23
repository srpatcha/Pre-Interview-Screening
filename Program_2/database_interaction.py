# database_interaction.py
import sqlite3

def connect_to_database(database_path):
    try:
        # Connect to database
        connection = sqlite3.connect(database_path)
        return connection

    except sqlite3.Error as e:
        return f"Failed to connect to the database: {str(e)}"


def execute_sql_query(connection, query):
    try:
        # Create a cursor object to SQL
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(query)

        # Commit the changes to database
        connection.commit()

        # Fetch the result
        result = cursor.fetchall()

        return result

    except sqlite3.Error as e:
        return f"Failed to execute SQL query: {str(e)}"


def close_database_connection(connection):
    try:
        # Close the connection
        connection.close()

    except sqlite3.Error as e:
        print(f"Error while closing the database connection: {str(e)}")
