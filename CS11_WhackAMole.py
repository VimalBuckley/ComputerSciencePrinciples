import turtle
import random
import os
from operator import itemgetter

global xClickThreshold
global yClickThreshold
global playerScore
global timeLeft
global playerName
s = turtle.Screen()
locations = [(-200, 150), (0, 150), (200, 150), (-200, 0), (0,0), (200, 0), (-200, -150), (0, -150), (200, -150)]
timerTurtle = turtle.Turtle()
scoringTurtle = turtle.Turtle()
turtles = []

def setup(numberOfTurtles):
    global xClickThreshold
    global yClickThreshold
    global playerScore
    global timeLeft
    global playerName
    os.system('cls')
    xClickThreshold = 10
    yClickThreshold = 10
    playerScore = 0
    timeLeft = 10
    s.bgcolor("red")
    timerTurtle.penup()
    timerTurtle.hideturtle()
    timerTurtle.speed(0)
    timerTurtle.goto(-250, 250)
    scoringTurtle.penup()
    scoringTurtle.hideturtle()
    scoringTurtle.speed(0)
    scoringTurtle.goto(-250, 200)
    scoringTurtle.write("Score: " + str(playerScore), font = ("Arial", 20, "normal"))
    for i in range(numberOfTurtles):
        turtles.append(turtle.Turtle())
    for t in turtles:
        t2: turtle = t
        t2.speed(0)
        t2.penup()
        turtle.register_shape("MoleV3.gif")
        t2.shape("MoleV3.gif")
    randomizeTurtleLocations()

def randomizeTurtleLocations():
    theseLocations = [(-200, 150), (0, 150), (200, 150), (-200, 0), (0,0), (200, 0), (-200, -150), (0, -150), (200, -150)]
    for t in turtles:
        t2: turtle = t
        thisLocation = random.choice(theseLocations)
        theseLocations.remove(thisLocation)
        t2.goto(thisLocation)
        t2.showturtle()

def clock():
    global timeLeft
    
    timeLeft -= 1
    if (timeLeft < 0):
        setDown()
    else:
        timerTurtle.clear()
        timerTurtle.write("Time left: " + str(timeLeft), font = ("Arial", 20, "normal"))
        randomizeTurtleLocations()
        s.ontimer(clock, 1000)

def clicked(x,y):
    global playerScore
    for t in turtles:
        t2: turtle = t
        if abs(t2.xcor() - x) < xClickThreshold and abs(t2.ycor() - y) < yClickThreshold:
            t2.hideturtle()
            t2.goto(1000,1000)
            playerScore += 1
            scoringTurtle.clear()
            scoringTurtle.write("Score: " + str(playerScore), font = ("Arial", 20, "normal"))

def setDown():
    print("Your score was: " + str(playerScore))
    s.bye()

def readScores(fileName: str = "CS11_Highscores.txt"):
    fileReader = open(fileName, "r")
    nameScoreList = []
    for line in fileReader:
        nameScoreList.append((line.split(": ")))
    fileReader.close()
    for pairing in nameScoreList:
        pairing[1] = int(pairing[1])
    return nameScoreList

def sortScores(nameScoreList: list):
    nameScoreList.sort(key = lambda x: x[1], reverse = True)
    return nameScoreList

def updateScores(playerScore: int, oldNameScoreList: list):
    playerName = input("What's your name? ")
    nameScoreList = sortScores(oldNameScoreList)
    playerPair = (playerName, playerScore)
    nameScoreList.append(playerPair)
    for pair in nameScoreList:
        if playerPair[0] == pair[0] and not playerPair == pair:
            if playerPair[1] > pair[1]:
                nameScoreList.remove(pair)
            else:
                nameScoreList.remove(playerPair)
            break
    nameScoreList = sortScores(nameScoreList)
    while len(nameScoreList) > 5:
        nameScoreList.pop()
    return nameScoreList

def writeScores(nameScoreList: list, fileName: str = "CS11_Highscores.txt"):
    fileWriter = open(fileName, "w")
    for pair in nameScoreList:
        fileWriter.write(pair[0] + ": " + str(pair[1]) + "\n")
    fileWriter.close()


def dealWithScoring():
    global playerName
    global playerScore
    nameList = []
    scoreList = []
    nameAndScoreList = []
    newNameList = []
    newScoreList = []
    foundPlace = False
    playerName = input("What's your name? ")
    info = open("CS11_Highscores.txt", "r")
    for line in info:
        name, score = line.split(",")
        score = score.split(" ")[0]
        nameList.append(name)
        scoreList.append(score)
        nameAndScoreList.append((name, score))
    info.close()
    foundMatch = False
    for nameScorePair in nameAndScoreList:
        if nameScorePair[0] == playerName:
            foundMatch = True
    for i in range(len(scoreList)):
        if int(scoreList[i]) < int(playerScore) and not foundPlace:
            newNameList.append(playerName)
            newScoreList.append(playerScore)
            print("You placed #" + str(i+1))
            foundPlace = True
        newNameList.append(nameList[i])
        newScoreList.append(scoreList[i])
    while len(newNameList) > 5:
        newNameList.pop()
        newScoreList.pop()
    file = open("CS11_Highscores.txt", "w")
    for i in range(len(nameList)):
        file.write(newNameList[i] + "," + str(newScoreList[i]) + " \n")
    file.close()

setup(4)
clock()
s.onclick(clicked)
s.mainloop()
writeScores(updateScores(playerScore, readScores()))
