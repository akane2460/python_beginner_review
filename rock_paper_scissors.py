# Python Tutorial for Beginners: Episode 10, Rock Paper Scissors Game
# import modules
from random import randint

# from loops import my_list

# define player moves
moves = ["rock", "paper", "scissors"]

while True:
    computer = moves[randint(0,2)]
    player = input("rock, paper or scissors? (or end game) ").lower()
    if player == "end game":
        print("The game has ended")
        break
    elif player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose! ", computer, " beats ", player)
        else:
            print("You win! ", player, " beats ", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose! ", computer, " beats ", player)
        else:
            print("You win! ", player, " beats ", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose! ", computer, " beats ", player)
        else:
            print("You win! ", player, " beats ", computer)
    else:
        print("Check your spelling")