import random
import string
import secrets

def generate_password(length=8):
    """
    Generate a random password of specified length,

    Args:
        length (int): Length of the password (default: 8)

    Returns:
        str: Generated password
    """
    # Define the character sets
    lowercase_letters = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    uppercase_letters = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = string.digits  # 0123456789
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    if length < 4:
        raise ValueError("Password length must be at least 4")

    # Combine all characters into one pool
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    rng = secrets.SystemRandom()

    # Ensure at least one character from each category
    password_chars = [
        rng.choice(lowercase_letters),
        rng.choice(uppercase_letters),
        rng.choice(digits),
        rng.choice(special_chars),
    ]

    # Fill the remaining length
    for _ in range(length - 4):
        password_chars.append(rng.choice(all_chars))

    # Shuffle to avoid predictable placement
    rng.shuffle(password_chars)

    return "".join(password_chars)

# Main program
if __name__ == "__main__":
    # Ask user for password length
    try:
        user_length = int(input("Enter password length (default is 8): ") or "8")
        if user_length < 4:
            print("Password length must be at least 4. Using default length of 8.")
            user_length = 8
    except ValueError:
        print("Invalid input. Using default length of 8.")
        user_length = 8

    # Generate and display the password
    new_password = generate_password(user_length)
    print("\nYour generated password is: ")
    print(new_password)

