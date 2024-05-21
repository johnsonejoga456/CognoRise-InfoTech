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
    
    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Convert list to string and return
    return ''.join(password)

def main():
    # Prompt the user for the desired password length
    length = int(input("Enter the desired length of the password: "))
    
    # Check if the length is sufficient to include all character types
    if length < 4:
        print("Password length should be at least 4 characters to ensure complexity.")
        return
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
