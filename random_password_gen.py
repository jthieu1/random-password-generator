# Creates a password using a combination of random letters, numbers, and special symbols

import random
import string


def pw_generator(length, lowercase=True, uppercase=True, digits=True, punctuation=True):
    """Uses lowercase letters, uppercase letters, numbers, and special symbols to add to characters for password"""
    characters = ""
    if lowercase:
        characters += string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if punctuation:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


#  user input for password generation
def gen_questions():
    prompting = None
    while prompting is None:
        length_choice = input("How many characters should the password be?: ")
        try:
            prompting = int(length_choice)
        except ValueError:
            print("Invalid. Please enter a valid number.")
            return gen_questions()
    if prompting > 0:
        generate = input("Would you like to generate a random password with personal preferences? (Yes or No): ").lower()
        if generate == "yes":
            lower_choice = input("Include lowercase letters? (Yes or No): ").lower()
            upper_choice = input("Include uppercase letters? (Yes or No): ").lower()
            digits_choice = input("Include numbers? (Yes or No): ").lower()
            punctuation_choice = input("Include special symbols? (Yes or No): ").lower()
            lowercase = True if lower_choice == "yes" else False
            uppercase = True if upper_choice == "yes" else False
            digits = True if digits_choice == "yes" else False
            punctuation = True if punctuation_choice == "yes" else False
            print("A password has been generated based off your preferences.")
            print(pw_generator(prompting, lowercase, uppercase, digits, punctuation))
        else:
            print("A random password has been generated with no preferences.")
            print(pw_generator(prompting))


gen_questions()
