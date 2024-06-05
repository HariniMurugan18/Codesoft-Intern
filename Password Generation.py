import string
import random

def generate_password(length, min_uppercase=1, min_lowercase=1, min_digits=1, min_special=1):
    if min_uppercase + min_lowercase + min_digits + min_special > length:
        raise ValueError("Minimum requirements exceed the total length of the password.")

    uppercase_letters = list(string.ascii_uppercase)
    lowercase_letters = list(string.ascii_lowercase)
    digits = list(string.digits)
    special_characters = list(string.punctuation)

    password = []
    password += random.sample(uppercase_letters, min_uppercase)
    password += random.sample(lowercase_letters, min_lowercase)
    password += random.sample(digits, min_digits)
    password += random.sample(special_characters, min_special)

    remaining_length = length - len(password)

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    password += random.choices(all_characters, k=remaining_length)

    random.shuffle(password)

    return ''.join(password)

def main():
    try:
       
        length = int(input("Enter the desired length of the password: "))

        min_uppercase = int(input("Enter the minimum number of uppercase letters: "))
        min_lowercase = int(input("Enter the minimum number of lowercase letters: "))
        min_digits = int(input("Enter the minimum number of digits: "))
        min_special = int(input("Enter the minimum number of special characters: "))

        if length < 1:
            print("Please enter a positive integer for the password length.")
            return

        password = generate_password(length, min_uppercase, min_lowercase, min_digits, min_special)

        print("Generated password:", password)
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
