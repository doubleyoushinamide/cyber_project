# This program splits inputs strings into lists and then turn it into a guessing
words = str(input("kindly input about 3 words of choice: \n"))
wordList = words.split(" ")

def compGuess():
    import random
    favWord = random.choice(wordList)
    return favWord

favWord = compGuess().lower()
#print(favWord)
wordCount = len(favWord)
#print (wordCount)
new = []
def harshes():
    i=0
    #new = []
    while i < wordCount:
        new.insert("*_*)
        i+=1

harshes()