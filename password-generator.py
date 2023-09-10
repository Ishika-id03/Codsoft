import random
import string

def generate_password(length):
    # Define character sets for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on desired complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Get user input for the desired password length
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer for the password length.")

# Generate and display the password
password = generate_password(length)
print(f"Generated Password: {password}")
