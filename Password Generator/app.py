import random
import string

def generate_password(length=8):
    """
    Generate a random password of specified length,

    Args:
        length (int): Length of the password (default: 8)

    Returns:
        str: Generated password
    """
    # Define the character sets
    lowercase_letters = string.ascii_lowercase #abcdefghijklmnopqrstuvwxyz
    uppercase_letters = string.ascii_uppercase #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = string.digits #0123456789
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    # Combine all characters into one pool
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Generate password by randomly selecting characters
    password = ""
    for _ in range(length):
    # Choose a random character from the pool and add it to the password
        random_char = random.choice(all_chars)
        password += random_char

    return password

# Main program
if __name__ == "__main__":
    # Ask user for password length
    try:
        user_length = int(input("Enter password length (default is 8): ") or "8")
        if user_length <= 0:
            print("Password length must be positive. Using default length of 8.")
            user_length = 8
    except ValueError:
        print("Invalid input. Using default length of 8.")
        user_length = 8

    # Generate and display the password
    new_password = generate_password(user_length)
    print("\nYour generated password is: ")
    print(new_password)