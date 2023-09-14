import CS2_Conditionals
import random

def rollTwoDiceMultipleTimes(times):
    for i in range(times):
        print(CS2_Conditionals.rollTwoDice())

def favoriteFoodsForPeople():
    people = ["Mickey", "Spongebob", "Mr. Krabs", "Patrick"]
    favoriteFoods = ["Pizza", "Spaghetti", "Lasanga", "General Tsos' Chicken"]

    for i in range(len(people)):
        print("The favorite food of", people[i], "is", favoriteFoods[i])

def countPractice():
    count = 0

    while count < 10:
        if count < 3:
            print("Long way to go")
        elif count < 6:
            print("Getting there")
        elif count < 9:
            print("So close")
        count += 1
    print("You made it!")

def playGuessingGame(min, max):
    playAgain = True
    timesPlayed = 0
    averageScore = 0
    currentScore = 0
    summedScores = 0
    while playAgain:
        randomNumber = random.randint(min,max)
        guess = int(input("Guess a number "))
        while guess != randomNumber:
            print("That's not correct!")
            currentScore += 1
            print("Your current score is " + str(currentScore))
            guess = int(input("Guess a new number: "))
        print("Correct")
        currentScore += 1
        timesPlayed += 1
        summedScores += currentScore
        averageScore = (summedScores) / timesPlayed
        print("Your average score is " + str(averageScore))
        currentScore = 0

        if input("Play again? y or n ") == "y":
            playAgain = True
            continue
        playAgain = False
        print("Thanks for playing!")

def rockPaperScissors(firstToWhat):
    playAgain = "y"
    allowedInputs = ["Rock", "Paper", "Scissors"]

    while playAgain == "y":
        computerScore = 0
        playerScore = 0
        while firstToWhat > computerScore and firstToWhat > playerScore:
            playerString = input("Rock, Paper, Scissors, Shoot! ")
            while not (playerString in allowedInputs):
                playerString = input(playerString + " isn't a valid option, pick again." + "\n" + "Rock, Paper, Scissors, Shoot! ")
            playerIndex = allowedInputs.index(playerString)
            computerIndex = random.randint(0,2)
            if playerIndex == computerIndex:
                print("Tie")
            elif computerIndex == playerIndex + 1 or computerIndex == playerIndex - 2:
                print("Computer scored")
                computerScore += 1
            else:
                playerScore += 1
                print("You scored")
            print("Your score is " + str(playerScore) + ". The computer's score is " + str(computerScore) + ".")
        if (computerScore > playerScore):
            print("Game over. Computer wins " + str(computerScore) + " to " + str(playerScore))
        else:
            print("Game over. Player wins " + str(playerScore) + " to " + str(computerScore))
        playAgain = input("Play again? y or n ")

