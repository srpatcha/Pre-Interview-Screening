# main.py
import threading
from password_validator import validate_passwords

def main():
    with open('subfolder/input_passwords.txt', 'r') as file:
        passwords = file.read().strip()

    thread1 = threading.Thread(target=validate_and_print_passwords, args=(passwords,))
    thread1.start()
    thread1.join()

def validate_and_print_passwords(passwords):
    valid_passwords = validate_passwords(passwords.split(','))
    print("Valid Passwords:", ', '.join(valid_passwords))

if __name__ == "__main__":
    main()