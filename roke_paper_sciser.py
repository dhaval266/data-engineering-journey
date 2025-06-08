import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

choice_emoji = {ROCK: "✊ Rock", PAPER: "✋ Paper", SCISSORS: "✌️ Scissors"}
choice = tuple(choice_emoji.keys())


def get_user_choice():
    while True:
        user_input = input("Enter your choice (r/p/s): ").lower()
        if user_input in choice:
            return user_input
        else:
            print("Invalid choice! Please enter 'r', 'p', or 's'.")
            continue


def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(
            f"Your choice: {choice_emoji[user_choice]}, computer's choice: {choice_emoji[computer_choice]}"
        )
        print("It's a tie!")

    elif (
        (user_choice == ROCK and computer_choice == SCISSORS)
        or (user_choice == PAPER and computer_choice == ROCK)
        or (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        print(
            f"Your choice: {choice_emoji[user_choice]}, computer's choice: {choice_emoji[computer_choice]}"
        )
        print("You win!")

    else:
        print(
            f"Your choice: {choice_emoji[user_choice]}, computer's choice: {choice_emoji[computer_choice]}"
        )
        print("You lose!")


def play_game():

    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choice)

        winner(user_choice, computer_choice)

        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again != "y" or play_again != "n":
            print("enter the valid input!")

        if play_again == "n":
            print("Thanks for playing!")
            break


play_game()
