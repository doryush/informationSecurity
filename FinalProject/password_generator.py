import random
import string
from colorama import Fore, Style
import pyfiglet

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("At least one character type must be selected.")
    
    return ''.join(random.choice(character_pool) for _ in range(length))

def save_passwords_to_file(passwords, filename="passwords.txt"):
    with open(filename, "a") as file:
        for password in passwords:
            file.write(password + "\n")
    print(Fore.GREEN + f"Passwords saved to {filename}")

def user_input():
    try:
        print(Fore.CYAN + pyfiglet.figlet_format("Pass Generator"))
        length = int(input("Enter password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
        use_digits = input("Include digits? (y/n): ").strip().lower() == "y"
        use_symbols = input("Include special characters? (y/n): ").strip().lower() == "y"
        num = int(input("How many passwords to generate? "))
        
        passwords = [generate_password(length, use_upper, use_lower, use_digits, use_symbols) for _ in range(num)]
        
        for pwd in passwords:
            print(Fore.YELLOW + pwd)
        
        save = input("Do you want to save passwords to a file? (y/n): ").strip().lower() == "y"
        if save:
            save_passwords_to_file(passwords)
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")

def main():
    user_input()

if __name__ == "__main__":
    main()

