

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        length = int(input("Enter the length of the password (default is 12): "))
        password = generate_password(length)

        print(f"Generated Password: {password}")

        regenerate = input("Do you want to generate another password? (yes/no): ").lower()
        if regenerate != "yes":
            print("Thanks for using the Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()