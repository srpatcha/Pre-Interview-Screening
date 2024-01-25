# password_validator.py
import re

def validate_passwords(passwords):
    valid_passwords = []

    for password in passwords:
        if (
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password) and
            re.search(r'[A-Z]', password) and
            re.search(r'[$#@]', password) and
            6 <= len(password) <= 12
        ):
            valid_passwords.append(password)

    return valid_passwords