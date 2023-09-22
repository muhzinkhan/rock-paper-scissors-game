import random
from os import system, name
from graphics import rock, paper, scissors, logo


game_images = [rock, paper, scissors]
play_game = True


def clear():
    """Clears the screen according to the os."""
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


def check(choice):
    valid = False
    while not valid:
        if choice in [0, 1, 2]:
            valid = True
        else:
            print("Enter a Valid choice like '0', '1', or '2.")
            choice = ask_choice()

    return choice


def ask_choice():
    return int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))


def play():
    print(logo)
    user_choice = check(ask_choice())
    print(f"You chose:\n{game_images[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"\nComputer chose:\n{game_images[computer_choice]}")

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win! 😊")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose 😓")
    elif computer_choice > user_choice:
        print("You lose 😓")
    elif user_choice > computer_choice:
        print("You win! 😊")
    elif computer_choice == user_choice:
        print("It's a draw")


while play_game:
    clear()
    play()
    play_game = True if input("Do you want to play again? (y/n): ").lower() == "y" else False
