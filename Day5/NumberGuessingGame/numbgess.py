import art
import random

EASY = 10
HARD = 5

computer_guess = random.randint(1,100)

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    attempts = EASY
elif difficulty == 'hard':
    attempts = HARD
else:
    print("Invalid input! Please enter 'easy' or 'hard'. Program Finished!")
    exit()

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess > computer_guess:
        print("Too high.")
        attempts -= 1
    elif user_guess < computer_guess:
        print("Too low.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {computer_guess}.")
        break
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The correct number was {computer_guess}.")
    else:
        print("Guess again.")

