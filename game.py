import random

choices = ["rock", "paper", "scissors"]
computer_points = 0
player_points = 0

while True:

    computer_choice = random.choice(choices)

    player_choice = input("Rock, Paper or Scissors?:").lower()

    if player_choice == "":
        break

    print("Computer picks " + computer_choice)

    if player_choice == computer_choice:
        print("Draw!")
    elif player_choice == "rock":
        if computer_choice == "paper":
            print("Computer wins!")
            computer_points += 1
        else:
            print("Player wins!")
            player_points += 1
    elif player_choice == "paper":
        if computer_choice == "scissors":
            print("Computer wins!")
            computer_points += 1
        else:
            print("Player wins!")
            player_points += 1
    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("Computer wins!")
            computer_points += 1
        else:
            print("Player wins!")
            player_points += 1
    else:
        print("Please pick a valid choice")

    print("Player score:", player_points)
    print("Computer score:", computer_points)