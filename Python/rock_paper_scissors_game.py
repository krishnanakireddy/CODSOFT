import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
    
def main():
    user_score = 0
    computer_score = 0

    print("\n-----Welcome to Rock, Paper, Scissors-----")
    print("Instructions:")
    print("Enter 'rock', 'paper', or 'scissors' to play.")
    print("Enter 'exit' to quit the game.\n")

    while True:
        user = input("Enter your choice (rock/paper/scissors) or 'exit' to quit: ").lower()
        if user == 'exit':
            print("Thanks for playing!")
            break
        if user not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer = get_computer_choice()
        print(f"Computer chose: {computer}")

        result = determine_winner(user, computer)
        print(result)

        if "You win!" in result:
            user_score += 1
        elif "Computer wins!" in result:
            computer_score += 1

        print(f"Score => You: {user_score}, Computer: {computer_score}\n")

if __name__ == "__main__":
    main()