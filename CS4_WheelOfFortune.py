import random

phrase = ""
phraseAsArray = []
clueAsArray = []
numberOfGuesses = 0
possiblePhrases = ["A CAT HAS NINE LIVES", "A BLESSING IN DISGUISE", "ANOTHER DAY ANOTHER DOLLAR", "BIG SHOES TO FILL"]
acceptedCharacters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def runGame(newPhrase = None):
    resetValues()
    if setPhrase(newPhrase):
        evaluateGuess()
        endGame("The phrase was: " + phrase + "\nGame over!")
    
def resetValues():
    global phrase
    global phraseAsArray
    global clue
    global clueAsArray
    global numberOfGuesses
    phrase = ""
    phraseAsArray = []
    clueAsArray = []
    numberOfGuesses = 0

def rollWheel():
    possiblePrizes = [200, 200, 200, 200, 400, 400, 900]
    prize = random.choice(possiblePrizes)
    print("\nYou're prize will be: " + str(prize))
    return prize

def setPhrase(newPhrase = None):
    global phrase
    if newPhrase == None:
        phrase = random.choice(possiblePhrases)
    else:
        phrase = newPhrase
        for letter in phrase:
            if letter not in acceptedCharacters and letter != " ":
                endGame("\nThe given phrase contains unaccepted characters")
                return False
    for letter in phrase:
        phraseAsArray.append(letter)
        if letter != " ":
            clueAsArray.append("_")
        else:
            clueAsArray.append(" ")
    return True

def evaluateGuess():
    global numberOfGuesses
    totalPrize = 0
    while "_" in clueAsArray:
        inPhrase = False
        numberOfGuesses += 1
        guess = ""
        frequency = 0
        prize = rollWheel()
        print(arrayToString(clueAsArray))
        while not guess in acceptedCharacters:
            guess = input("Guess a uppercase letter: ")
        for i in range(len(phraseAsArray)):
            if guess == phraseAsArray[i]:
                clueAsArray[i] = guess
                frequency += 1
                inPhrase = True  
        print("Number of times " + guess + " appeared: " + str(frequency))
        if inPhrase:
            print("You earned " + str(prize) + " dollars")
            totalPrize += prize
        print("Number of guesses so far: " + str(numberOfGuesses))
    print("\nIn this game, you earned " + str(totalPrize) + " dollars in total!")
        
def endGame(endMessage):
    print(endMessage)

def arrayToString(desiredArray):
    tempString = ""
    for element in desiredArray:
        tempString = tempString + element 
    return tempString


