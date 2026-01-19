import alphabets
shifted_alphabets = []

def encrypt():
    text = input("Enter the text to be ciphered: ").lower()
    shifted_alphabets.clear()
    shifted_alphabets.extend(alphabets.original_alphabets[shift:])
    shifted_alphabets.extend(alphabets.original_alphabets[:shift])
    ciphered_text = ""
    for char in text:
        if char in alphabets.original_alphabets:
            index = alphabets.original_alphabets.index(char)
            ciphered_text += shifted_alphabets[index]
        else:
            ciphered_text += char
    print(f"Ciphered Text: {ciphered_text}")

def decrypt():
    text = input("Enter the text to be deciphered: ").lower()
    shifted_alphabets.clear()
    shifted_alphabets.extend(alphabets.original_alphabets[shift:])
    shifted_alphabets.extend(alphabets.original_alphabets[:shift])
    deciphered_text = ""
    for char in text:
        if char in shifted_alphabets:
            index = shifted_alphabets.index(char)
            deciphered_text += alphabets.original_alphabets[index]
        else:
            deciphered_text += char
    print(f"Deciphered Text: {deciphered_text}")

def caesar_cipher(shift,decision):
    if(decision == 'encode'):
        encrypt()
    elif(decision == 'decode'):
        decrypt()
    else:
        print("Invalid decision! Please enter 'encode' or 'decode'.")
   
    
print("Welcome to Caesar Cipher!")
play = "yes"
while(play):
     play = input("Do you want to encode or decode a message? 'Yes' to continue, 'No' to exit.").lower()
     if(play == 'no'):
         print("Exiting the program. Goodbye!")
         break
     elif(play == 'yes'):
         decision = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
         if(decision not in ['encode','decode']):
             print("Invalid input! Please enter 'encode' or 'decode'.")
             continue
         shift = int(input("Enter the shift value (1-25): "))
         if(shift < 1 or shift > 25):
             print("Invalid shift value! Please enter a value between 1 and 25.")
         else:
             caesar_cipher(shift,decision)