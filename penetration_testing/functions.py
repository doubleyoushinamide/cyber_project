# This program splits inputs strings into lists and then turn it into a guessing game
words = str(input("kindly input about 3 words of choice: \n"))
wordList = words.split(" ")

def compGuess():
    import random
    favWord = random.choice(wordList)
    return favWord

userWord = str(input("Guess a word that I'd written \n")).lower()
Guess = compGuess().lower()
#print(userWord)

if userWord == Guess:
    print("You guessed correctly!")
else:
    print("Try again!")

#print (wordList)