import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose from rock, paper, or scissors.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "win"
    else:
        return "lose"

def display_result(user_choice, computer_choice, result):
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    print(f"You {result}!")

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"Your score: {user_score}, Computer's score: {computer_score}")

        if not play_again():
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
