import random

while True:
    chois = ["rock", "paper", "scissors"]

    player = None
    computer = str(random.choices(chois))   # typecasting list item into str to slice it afterwards
    computer = computer[slice(2,-2)]        # mantaining bug which puts [''] importing value from list

    while player not in chois:
        player = input("Rock, paper or scissors?: ").lower()

    if player == computer:
        print("Computer:",computer)
        print("Player:",player)
        print("That's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        elif computer == "scissors":
            print("Computer:",computer)
            print("Player:",player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        elif computer == "rock":
            print("Computer:",computer)
            print("Player:",player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        elif computer == "paper":
            print("Computer:",computer)
            print("Player:",player)
            print("You win!")
    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        break
print("Bye!")