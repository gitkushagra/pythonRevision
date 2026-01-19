import art
import random

decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if decision == 'y':
    print(art.logo)
elif decision == 'n':
    print("Maybe next time! Goodbye!")
    exit()
else:
    print("Invalid input! Please type 'y' or 'n'. Program Finished!")
    exit()
    
user_cards = []
computer_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def newComputerCard(computer_cards):
    newCard = deal_card()
    currentComputerSun = sum(computer_cards)
    if newCard == 11:
        if currentComputerSun + 11 < 21:
            return newCard
        else:
            return 1
    else:
        return newCard

def newUserCard(user_cards):
    newCard = deal_card()
    if newCard == 11:
        print("Hey, you got an Ace!")
        choose = input("Do you want it to be 1 or 11? Type '1' or '11': ")
        if choose == '11':
            return 11
        else:   
            return 1
    else:
        return newCard

def game_decision(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose!"
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 21:
        return "Lose, opponent has Blackjack! You lose!"
    elif user_score == 21:
        return "Win with a Blackjack! You win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:  
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win! Your score is higher."
    else:
        return "No Decision"

user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card()) 
print(f"   Your cards: {user_cards}, current score: {sum(user_cards)}")
print(f"   Computer's first card: {computer_cards[0]}")
game_over = False


while not game_over:
    userDeal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if userDeal == 'y':
        computer_cards.append(newComputerCard(computer_cards))
        user_cards.append(newUserCard(user_cards))
        print(f"   Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"   Computer's first card: {computer_cards[0]}")
        decision = game_decision(sum(user_cards), sum(computer_cards))
        if decision != "No Decision":
            print(decision)
            game_over = True
    elif userDeal == 'n':
        computerDecidingCard = newComputerCard(computer_cards)
        currentComputerSum = sum(computer_cards)
        if currentComputerSum + computerDecidingCard <= 21:
            computer_cards.append(computerDecidingCard)
        print(f"   Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"   Computer's first card: {computer_cards[0]}")
        decision = game_decision(sum(user_cards), sum(computer_cards))
        if decision != "No Decision":
            print(decision)
            game_over = True