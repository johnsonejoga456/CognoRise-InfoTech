import random
import string

def generate_password(length):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all character sets
    all_characters = lower + upper + digits + special
    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def main():
    # Prompt the user for the desired password length
    length = int(input("Enter the desired length of the password: "))
    
    if length < 4:
        print("Password length should be at least 4 characters to ensure complexity.")
        return
    
    password = generate_password(length)
    
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
