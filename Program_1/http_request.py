# http_request.py
import requests

def make_https_request(url):
    try:
        response = requests.get(url, verify=True)  
        response.raise_for_status()
        return response.text

    except requests.exceptions.RequestException as e:
        return f"Failed HTTP request: {str(e)}"