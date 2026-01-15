print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
numOfPeople = int(input("How many people to split the bill? "))
eachPay = (bill * (tip+100)/100) / numOfPeople
print(f"Each person should pay: ${eachPay:.2f}")