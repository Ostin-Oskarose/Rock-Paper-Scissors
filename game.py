import random

choices = ["rock", "paper", "scissors"]
computerPoints = 0
playerPoints = 0

while True:

    computerChoice = random.choice(choices)

    playerChoice = input("Rock, Paper or Scissors?:").lower()

    if playerChoice == "":
        break

    print("Computer picks " + computerChoice)

    if playerChoice == computerChoice:
        print("Draw!")
    elif playerChoice == "rock":
        if computerChoice == "paper":
            print("Computer wins!")
            computerPoints += 1
        else:
            print("Player wins!")
            playerPoints += 1
    elif playerChoice == "paper":
        if computerChoice == "scissors":
            print("Computer wins!")
            computerPoints += 1
        else:
            print("Player wins!")
            playerPoints += 1
    elif playerChoice == "scissors":
        if computerChoice == "rock":
            print("Computer wins!")
            computerPoints += 1
        else:
            print("Player wins!")
            playerPoints += 1
    else:
        print("Please pick a valid choice")

    print("Player score:", playerPoints)
    print("Computer score:", computerPoints)