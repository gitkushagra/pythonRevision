def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def power(num1, num2):
    return num1 ** num2 
def modulo(num1, num2):
    return num1 % num2



def calculation(fields):
    if fields[0] == '+':
        return add(fields[1], fields[2])
    elif fields[0] == '-':
        return subtract(fields[1], fields[2])
    elif fields[0] == '*':
        return multiply(fields[1], fields[2])
    elif fields[0] == '/':
        if(fields[2] == 0):
            return "Error! Division by zero."
        return divide(fields[1], fields[2])
    elif fields[0] == '^':
        return power(fields[1], fields[2])
    elif fields[0] == '%':
        return modulo(fields[1], fields[2])
    else:
        return "Invalid operation!"
    
def askOperation():
    operation = input("Enter operation (+, -, *, /, ^, %): ")
    return operation
    
def askUser(result):
    if result is None:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = askOperation()
        return operation, num1, num2
    else:
       num1 = result
       num2 = float(input("Enter next number: "))
       operation = askOperation()
       return operation, num1, num2

def calculator():
    print("Welcome to the Calculator!")
    result = None
    decision = 'yes'
    while decision == 'yes':
        fields = askUser(result)
        prevResult = result
        result = calculation(fields)
        if result == "Error! Division by zero." or result == "Invalid operation!":
            print(f"Please enter valid inputs to continue with {prevResult: .2f}")
            result = prevResult
            continue
        print(f"Result: {result: .2f}")
        decision = input(f"Do you want to continue calculating with the {result: .2f}? Type 'yes' or 'no': ").lower()
        if decision == 'no':
            print("Exiting the calculator. Goodbye!")
        elif decision !='yes':
            while(True):
                print("Invalid input! Please type 'yes' or 'no'.")
                decision = input(f"Do you want to continue calculating with the {result: .2f}? Type 'yes' or 'no': ").lower()
                if decision in ['yes','no']:
                    break
                

calculator()           

            

