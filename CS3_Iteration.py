import CS2_Conditionals
import random
import os

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
        os.system("cls")
        computerScore = 0
        playerScore = 0
        while firstToWhat > computerScore and firstToWhat > playerScore:
            playerString = input("Rock, Paper, Scissors, Shoot! ")
            while not (playerString in allowedInputs):
                playerString = input(playerString + " isn't a valid option, pick again." + "\n" + "Rock, Paper, Scissors, Shoot! ")
            computerRandomNumber = random.randint(0,2)
            for i in range(computerRandomNumber):
                temp = allowedInputs.copy()
                allowedInputs.clear()
                allowedInputs.append(temp[2])
                allowedInputs.append(temp[0])
                allowedInputs.append(temp[1])
            print("You chose", playerString)
            print("The computer chose", allowedInputs[2])
            if playerString == allowedInputs[0]:
                print("You scored")
                playerScore += 1
            elif playerString == allowedInputs[1]:
                print("Computer scored")
                computerScore += 1
            else:
                print("Tie")
            print("Your score is " + str(playerScore) + ". \nThe computer's score is " + str(computerScore) + ".\n")
        if (computerScore > playerScore):
            print("Game over. Computer wins " + str(computerScore) + " to " + str(playerScore))
        else:
            print("Game over. Player wins " + str(playerScore) + " to " + str(computerScore))
        playAgain = input("Play again? y or n ")
