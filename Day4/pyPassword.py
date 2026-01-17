import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '@','#','$','%','^','&','*','(',')','-']

print("Welcome to the PyPassword Generator!")
no_alphabets = int(input("How many alphabets would you like in your password?\n"))
no_numbers = int(input("How many numbers would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like in your password?\n"))

password_list = []
choseAlphatbets = random.choices(alphabets,k = no_alphabets)
password_list.extend(choseAlphatbets)
choseNumbers = random.choices(numbers,k = no_numbers)
password_list.extend(choseNumbers)
choseSymbols = random.choices(symbols,k =  no_symbols)
password_list.extend(choseSymbols)
random.shuffle(password_list)
password = ''.join(password_list)
print(f"Your password is: {password}")