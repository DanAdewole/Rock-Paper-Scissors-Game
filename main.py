import random

print("Welcome to my game of Rock, Paper and Scissors")
choices = ["R", "P", "S"]

game_on = True
while game_on:
    user_choice = input("Enter 'R' for Rock, 'P' for Paper and 'S' for Scissors: ").title()
    if user_choice not in choices:
        print("Error. Start again.")
    else:
        computer_choice = random.choice(choices)
        print(f"Player ({user_choice}) : CPU ({computer_choice})")
        if user_choice == computer_choice:
            print("The game is a tie. Start again.")
        elif (user_choice == "R" and computer_choice == "S") or (user_choice == "P" and computer_choice == "R") or \
                (user_choice == "S" and computer_choice == "P"):
            print("You win")
            game_on = False
        else:
            print("You lose")
            game_on = False
