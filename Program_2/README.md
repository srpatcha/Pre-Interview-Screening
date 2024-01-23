# Microsoft Pre-Interview-Screening programming 2
# SQL Database Automation over Server Requests

1. Clone the repository: git clone git@github.com:srpatcha/Pre-Interview-Screening.git
2. Install dependencies (`pip install requests`).
3. Ensure you have SQLite installed for database interaction.
4. Keep the URL in the `subfolder/input.txt` update URL https://google.com to  jdbc:sqlserver://<dbhost>:<dbport>
   Example : "jdbc:sqlserver://<server>:<port>";
           : "jdbc:sqlserver://<server>:<port>;encrypt=true;databaseName=AdventureWorks;user=<user>;password=<password>";

5. Run the main.py file to execute the program.

## Code Structure

- `database_interaction.py`: Contains functions for SQLite database interaction with exception handling.
- `server_request.py`: Contains functions for making server requests with exception handling.
- `main.py`: Calls functions to demonstrate SQL database automation over server requests.
- `subfolder/input.txt`: Input file.

## Execute the following command in the bash terminal:

python main.py

# Run unit tests using pytest testing framework
pytest database_interaction.py server_request.py