
import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        print("\nChoose character types (yes/no):")

        uppercase = input("Include uppercase letters? ").lower()
        lowercase = input("Include lowercase letters? ").lower()
        numbers = input("Include numbers? ").lower()
        symbols = input("Include special symbols? ").lower()

        if any(choice not in ["yes", "no"] for choice in
               [uppercase, lowercase, numbers, symbols]):
            print("Please enter only yes or no.")
            continue

        character_sets = []

        if uppercase == "yes":
            character_sets.append(string.ascii_uppercase)

        if lowercase == "yes":
            character_sets.append(string.ascii_lowercase)

        if numbers == "yes":
            character_sets.append(string.digits)

        if symbols == "yes":
            character_sets.append(string.punctuation)

        if len(character_sets) < 2:
            print("Please select at least two character types.")
            continue

        all_characters = "".join(character_sets)

        password = [
            random.choice(characters)
            for characters in character_sets
        ]

        while len(password) < length:
            password.append(random.choice(all_characters))

        random.shuffle(password)

        generated_password = "".join(password)

        print("\nYour generated password:", generated_password)

        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")
