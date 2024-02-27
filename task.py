import random
import string

def generate_password(length):
    # Define the character sets for each type of character
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate the password randomly
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    # Generate and print the specified number of passwords6
    for _ in range(num_passwords):
        password = generate_password(password_length)
        print(password)

if __name__ == "__main__":
    main()
