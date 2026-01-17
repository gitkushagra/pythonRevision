import random
import wordList
import stage

chosen_word = list(random.choice(wordList.words))

print("Welcome to Hangman!")
print("Total lives: "+str(len(stage.stages)))
wordLen = len(chosen_word) 
display = []
for _ in range(wordLen):
    display.append("_")
print("".join(display))
sindex = 6
windex = 0
while(wordLen > 0):
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        print(stage.stages[sindex])
        sindex -= 1
        if sindex < 0:
            print("You lost! The word was: " + "".join(chosen_word))
            break
    else:
        if guess in display:
            print("You have already guessed that letter. Try again.")
            continue
        for letter in chosen_word:
            if letter == guess:
                display[windex] = guess
                wordLen -= 1
            windex += 1
        windex = 0
        print("".join(display))
if wordLen == 0:
  print("You win! The word was: " + "".join(chosen_word))


