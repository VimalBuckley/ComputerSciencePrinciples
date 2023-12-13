import random

def resetValues():
    global score
    score = 0
    global phrase
    phrase = ""
    global lives
    lives = 3
    global prize
    prize = 0
    global clue
    clue = ""
    global guess
    guess = ""
    global playGame
    playGame = True
    global guessedCharacters
    guessedCharacters = [" "]

def getPossiblePhrases():
    return ["A CAT HAS NINE LIVES", "A BLESSING IN DISGUISE", "ANOTHER DAY ANOTHER DOLLAR", "BIG SHOES TO FILL"]

def getAcceptedInputs():
    return ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
def setPhrase(newPhrase = None):
    global phrase
    if newPhrase != None:
        phrase = newPhrase
    else:
        phrase = random.choice(getPossiblePhrases())

def listToString(listToConvert):
    return "".join(listToConvert)

def convertPhrase():
    clue = []
    for letter in phrase:
        if letter in guessedCharacters:
            clue.append(letter)
        else:
            clue.append("_")
    return clue

def spinWheel():
    global prize
    possilblePrizes = [100, 100, 100, 100, 200, 200, 200, 300, 300, 500, "Bankrupt"]
    print("\nYou spun the wheel!")
    prize = random.choice(possilblePrizes)
    if prize == "Bankrupt":
        possilblePrizes.pop()
        print("You went bankrupt! Your score is now zero!")
        print("You're rolling again!")
        prize = random.choice(possilblePrizes)
    print("Your possible prize for the next round is", prize, "points! Good luck!")
     
def playerGuess():
    global guess
    print(listToString(convertPhrase()))
    validGuess = False
    guess = input("Choose an uppercase letter: ")
    while not validGuess:
        if guess not in getAcceptedInputs():
            guess = input("That isn't a valid guess. Please guess again: ")
        elif guess in guessedCharacters:
            guess = input("You've already guessed that. Please guess again: ")
        else:
            validGuess = True
    guessedCharacters.append(guess)

def checkGuess():
    if guess in phrase:
        return True
    return False

def summarizeRound():
    global lives
    global score
    if checkGuess():
        print("Your guess was in the phrase!")
        print("Your prize was added to your score!")
        score += prize
    else:
        print("Your guess wasn't in the phrase!")
        print("You lost a life")
        lives -= 1
    print("Stat Summary: Score:", score, "| Lives left:", lives)
    if lives > 0:
        if "_" not in convertPhrase():
            endGame(True)
    else:
        endGame(False)

def endGame(won):
    global playGame
    playGame = False
    print("\n")
    if won:
        print("Congraulations, you guessed the phrase:", phrase)
        print("You earned $" + str(score) + "!")
    else:
        print("You ran out of lives :(")
        print("The phrase was:", phrase)
        print("Game Over!")
    
def runGame(gamePhrase = None):
    resetValues()
    setPhrase(gamePhrase)
    while playGame:
        spinWheel()
        playerGuess()
        summarizeRound()