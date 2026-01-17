import random

def result(userChoice, computerChoice):
    print(f"Computer chose: {computerChoice} \n")
    if userChoice == "rock" and computerChoice == "scissor":
        print("You win!")
    elif userChoice == "paper" and computerChoice == "rock":
        print("You win!")
    elif userChoice == "scissor" and computerChoice == "paper":
        print("You win!")
    elif userChoice == "rock" and computerChoice == "paper":
        print("You lose!")
    elif userChoice == "paper" and computerChoice == "scissor":
        print("You lose!")
    elif userChoice == "scissor" and computerChoice == "rock":
        print("You lose!")
    else:
        print("It's a draw!")

choice = ["rock", "paper", "scissor"]
key = True
userChoice = input("What do you choose? Type Rock or Paper or Scissor.\n").lower()
computerChoice = None
if userChoice not in choice:
    print("Invalid choice! You lose.")
    key = False
else:
    print(f"You chose: {userChoice} \n")

if key:
    computerChoice = random.choice(choice)
    result(userChoice, computerChoice)

