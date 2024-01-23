# main.py
import threading
from http_request import make_https_request
from web_automation import automate_web_interaction

def main():
    with open('subfolder/input.txt', 'r') as file:
        url = file.read().strip()

    thread1 = threading.Thread(target=make_https_request, args=(url,))
    thread2 = threading.Thread(target=automate_web_interaction, args=(url,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
