import string
import secrets


def generate_password(length):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digit = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digit + symbols
    password = ''
    # Generate Password
    for _ in range(length):
        password += secrets.choice(all_characters)

    return password

