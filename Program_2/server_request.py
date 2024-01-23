# server_request.py
import requests

def make_server_request(url):
    try:
        # To server request
        response = requests.get(url)

        # Response status code
        response.raise_for_status()

        return response.text

    except requests.exceptions.RequestException as e:
        return f"Failed server request: {str(e)}"
