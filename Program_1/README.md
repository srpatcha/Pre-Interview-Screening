# Microsoft ////////// Pre-interview Full Stack Automation over HTTPS programming 1 

## Instructions

1. Clone the repository : git clone git@github.com:srpatcha/Pre-Interview-Screening.git
2. Install dependencies (`pip install requests selenium`).
3. Ensure you have Chrome installed for web automation.
4. Keep the URL in the `subfolder/input.txt` update URL https://google.com to https://www.safecodeg.com/
5. Run the main.py file to execute the program.

## Code Structure

- `http_request.py`: Contains functions for making HTTPS requests with exception handling.
- `web_automation.py`: Contains functions for web automation using Selenium with exception handling.
- `main.py`: Calls functions to demonstrate full-stack automation.
- `subfolder/input.txt`: Input file.

## Execute the following command in the bash terminal:

python main.py

# Unit tests using pytest testing framework
pytest http_request.py web_automation.py
