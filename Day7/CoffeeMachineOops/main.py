from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

while True:
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    choice  = input(f"What would you like? ({menu.get_items()}): ").lower()
    
    if choice == "off":
        print("Turning off the coffee machine. Goodbye!")
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(choice)
        if coffee != None:
           if coffee_maker.is_resource_sufficient(coffee):
              if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)

