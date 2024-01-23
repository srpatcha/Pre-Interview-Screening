# main.py
import threading
from database_interaction import connect_to_database, execute_sql_query, close_database_connection
from server_request import make_server_request

def main():
    # Read inputs from a file located in a separate sub-folder
    with open('subfolder/input.txt', 'r') as file:
        database_path = file.readline().strip()
        sql_query = file.readline().strip()
        server_url = file.readline().strip()

    # Run each algorithm in parallel with multi-thread processing
    thread1 = threading.Thread(target=database_interaction, args=(database_path, sql_query,))
    thread2 = threading.Thread(target=server_interaction, args=(server_url,))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for all threads to finish
    thread1.join()
    thread2.join()

def database_interaction(database_path, sql_query):
    # Connect to database
    connection = connect_to_database(database_path)

    if isinstance(connection, sqlite3.Connection):
        # Execute SQL query
        result = execute_sql_query(connection, sql_query)
        print(f"Database Result: {result}")

        # Close the database connection
        close_database_connection(connection)
    else:
        print(connection)

def server_interaction(server_url):
    # server request
    result = make_server_request(server_url)
    print(f"Server Result: {result}")

if __name__ == "__main__":
    main()
