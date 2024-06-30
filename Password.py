import string
import random

def get_user_input():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError("Password length should be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None, None
    
    print('''Choose character set for password from these: 
            1. Letters
            2. Digits
            3. Special characters
            4. Done''')

    characterList = ""
    
    while True:
        try:
            choice = int(input("Pick a number (1-4): "))
            if choice == 1:
                characterList += string.ascii_letters
                print("Letters added.")
            elif choice == 2:
                characterList += string.digits
                print("Digits added.")
            elif choice == 3:
                characterList += string.punctuation
                print("Special characters added.")
            elif choice == 4:
                if characterList:
                    break
                else:
                    print("No character set selected. Please select at least one character set.")
            else:
                print("Please pick a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")
    
    return length, characterList

def generate_password(length, characterList):
    if not characterList:
        return None
    password = ''.join(random.choice(characterList) for _ in range(length))
    return password

def main():
    length, characterList = get_user_input()
    if length and characterList:
        password = generate_password(length, characterList)
        if password:
            print("The random password is:", password)
        else:
            print("Failed to generate password.")
    
        print("Password generation aborted due to invalid inputs.")

if __name__ == "__main__":
    main()
