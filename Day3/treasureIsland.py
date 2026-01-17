print("Welcome to Treasure Island. Your mission is to find the treasure.\n")
direction = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right": ').lower()
if direction != "left":
    print("You fell into a hole. Game Over.")
else:
    swimDecision = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
    if swimDecision != "wait":
        print("You get attacked by an angry trout. Game Over.")
    else:
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
                   