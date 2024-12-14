import random

# Choices for the game
choices = ["Rock", "Paper", "Scissors"]

# Initialize scores, game history, and power-up status
user_score = 0
computer_score = 0
tie_score = 0
user_streak = 0
user_power_up = False
game_history = []

def display_rules():
    print("\n--- GAME RULES ---")
    print("1. Rock crushes Scissors.")
    print("2. Scissors cuts Paper.")
    print("3. Paper covers Rock.")
    print("\n--- POWER-UP RULE ---")
    print("Win 3 rounds in a row to earn a 'Double Damage' Power-Up!")
    print("Use the Power-Up to double your score for the next win.\n")

def get_user_choice():
    print("Choices: ", ", ".join([f"{i+1}. {choice}" for i, choice in enumerate(choices)]))
    try:
        user_input = int(input("Enter your choice (1-3): ")) - 1
        if user_input in range(len(choices)):
            return choices[user_input]
        else:
            print("Invalid choice. Try again.")
            return get_user_choice()
    except ValueError:
        print("Please enter a valid number.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(choices)

def play_round():
    global user_score, computer_score, tie_score, user_streak, user_power_up
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
        tie_score += 1
        user_streak = 0  # Reset streak on tie
        game_history.append(f"Round {len(game_history) + 1}: Tie (Both chose {user_choice})")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        if user_power_up:
            print(f"Double Damage! You win! {user_choice} beats {computer_choice}.")
            user_score += 2  # Double score
            user_power_up = False  # Use up the power-up
        else:
            print(f"You win! {user_choice} beats {computer_choice}.")
            user_score += 1
        
        user_streak += 1
        if user_streak == 3:
            print("Congratulations! You've earned a 'Double Damage' Power-Up!")
            user_power_up = True
            user_streak = 0  # Reset streak after earning power-up
        
        game_history.append(f"Round {len(game_history) + 1}: You won! ({user_choice} beats {computer_choice})")
    else:
        print(f"You lose! {computer_choice} beats {user_choice}.")
        computer_score += 1
        user_streak = 0  # Reset streak on loss
        user_power_up = False  # Lose power-up if unused
        game_history.append(f"Round {len(game_history) + 1}: You lost! ({computer_choice} beats {user_choice})")

def display_scores():
    print("\n--- SCORES ---")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {tie_score}")
    print(f"Power-Up Status: {'Available' if user_power_up else 'Not Available'}")

def display_game_history():
    print("\n--- GAME HISTORY ---")
    for record in game_history:
        print(record)

def main():
    display_rules()
    print("Welcome to Rock-Paper-Scissors with Power-Ups!")
    while True:
        play_round()
        display_scores()
        print("\nDo you want to play another round? (y/n)")
        play_again = input("Enter 'y' to continue or 'n' to quit: ").lower()
        if play_again == 'n':
            break

    print("\nThanks for playing! Here's your game summary:")
    display_game_history()
    display_scores()
    print("Goodbye! See you next time!")

if __name__ == "__main__":
    main()
