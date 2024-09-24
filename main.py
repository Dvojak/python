import random
list = ["rock", "paper", "scissors"]

try_again = "y"

while try_again == "y" or try_again == "":
    user_input = input("Choose rock, paper or scissors :")
    if user_input == list[0] or user_input == list[1] or user_input == list[2]:
        if user_input == "rock" and random.choice(list) == "scissors":
            print("Opponent chose scissors")
            print("You win")
        elif user_input == "paper" and random.choice(list) == "rock":
            print("Opponent chose rock")
            print("You win")
        elif user_input == "scissors" and random.choice(list) == "paper":
            print("Opponent chose paper")
            print("You win")
        elif user_input == random.choice(list):
            print("You picked the same thing")
            print("draw")
        else:

            print("You lose")

    else:
        print("Wrong input")
    try_again = input("Do you want to continue?:")