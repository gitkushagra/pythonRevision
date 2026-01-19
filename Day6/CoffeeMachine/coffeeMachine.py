import resources
import emojiCollection

def is_resource_sufficient(coffee):
    """Check reource sufficiency"""
    if resources.resource["resources"]["water"] < resources.resource[coffee]["water"]:
        print(f"Sorry there is not enough water {emojiCollection.water}.")
        return False
    if resources.resource["resources"]["milk"] < resources.resource[coffee]["milk"]:
        print(f"Sorry there is not enough milk {emojiCollection.milk}.")
        return False
    if resources.resource["resources"]["coffee"] < resources.resource[coffee]["coffee"]:
        print(f"Sorry there is not enough coffee {emojiCollection.coffee_bean}.")
        return False
    return True

def process_resources(coffee):
    """Deduct the required resources from the machine."""
    resources.resource["resources"]["water"] -= resources.resource[coffee]["water"]
    resources.resource["resources"]["milk"] -= resources.resource[coffee]["milk"]
    resources.resource["resources"]["coffee"] -= resources.resource[coffee]["coffee"]
    resources.resource["resources"]["money"] += resources.resource[coffee]["cost"]

def process_coins():
    """Process coins inserted by the user."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

while True:
    print("Welcome to the Coffee Machine!")
    choice = input("What would you like? (espresso/latte/cappuccino): ").upper()
    if choice == "OFF":
        print(f"Turning off the coffee machine. Goodbye! {emojiCollection.bye}")
        break
    elif choice == "REPORT":
        print(f"{emojiCollection.water} Water: {resources.resource['resources']['water']}ml")
        print(f"{emojiCollection.milk} Milk: {resources.resource['resources']['milk']}ml")
        print(f"{emojiCollection.coffee_bean} Coffee: {resources.resource['resources']['coffee']}g")
        print(f"{emojiCollection.money} Money: ${resources.resource['resources']['money'] :.2f}")
    elif choice in resources.resource:
        coffee = choice
        if is_resource_sufficient(coffee):
            payment = process_coins()
            if payment >= resources.resource[coffee]["cost"]:
                change = round(payment - resources.resource[coffee]["cost"], 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                process_resources(coffee)
                print(f"Here is your {coffee.lower()} {emojiCollection.coffee_cup}. Enjoy!")
            else:
                print(f"Sorry that's not enough money. Money refunded. {emojiCollection.money} ")
        else:
            print(f"Cannot process your order due to insufficient resources. {emojiCollection.error}")
    else:
        print(f"Invalid selection. Please choose espresso, latte, or cappuccino. {emojiCollection.userError}")


