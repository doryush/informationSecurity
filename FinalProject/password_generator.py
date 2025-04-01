import random
import string
from colorama import Fore, Style
import pyfiglet

def generatePassword(length=7, useUpper=True, useLower=True, useDigits=True, useSymbols=True):
    passwordFull = ""
    if useUpper == True:
        passwordFull += string.ascii_uppercase
    if useLower == True:
        passwordFull += string.ascii_lowercase
    if useDigits == True:
        passwordFull += string.digits
    if useSymbols == True:
        passwordFull += string.punctuation
    
    if not passwordFull:
        raise ValueError("Please choose at least one character type.")   
    return ''.join(random.choice(passwordFull) for _ in range(length))

def savePasswords(passwords, filename="passwordsGenerated.txt"):
    with open(filename, "a") as file:
        for password in passwords:
            file.write(password + "\n")
    print(Fore.GREEN + f"Passwords have been saved to {filename}")

def userInput():
    try:
        print(Fore.CYAN + pyfiglet.figlet_format("Pass Generator"))
        lengthForPass = int(input("Enter password length: "))
        useUpper = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
        useLower = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
        useDigits = input("Include digits? (y/n): ").strip().lower() == "y"
        useSymbols = input("Include special characters? (y/n): ").strip().lower() == "y"
        num = int(input("How many passwords do you want to generate? "))
        
        passwords = [generatePassword(lengthForPass, useUpper, useLower, useDigits, useSymbols) for _ in range(num)]
        
        for pwd in passwords:
            print(Fore.GREEN + pwd)
        
        save = input("Do you want to save passwords to a file? (y/n): ").strip().lower() == "y"
        if save == True:
            savePasswords(passwords)
    except ValueError as e:
        print(Fore.RED + f"Error: {e}")

def main():
    userInput()

if __name__ == "__main__":
    main()

