import re
import string
import secrets


def generate_password(length,nums,special_chars,uppercase,lowercase):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digit = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digit + symbols

    while True:
        password = ''
        # Generate Password
        for _ in range(length):
            password += secrets.choice(all_characters)

        
        constraints = [
            (nums, r'\d'), # [0-9]
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars, r'\W') # [^a-zA-Z0-9]
        ]           

        return password

