import turtle
import random
import os

screen = turtle.Screen()
timerTurtle = turtle.Turtle()
scoringTurtle = turtle.Turtle()
turtles = []

def setup(numberOfTurtles):
    global playerScore
    global timeLeft
    os.system('cls')
    playerScore = 0
    timeLeft = 10
    screen.bgcolor("red")
    timerTurtle.penup()
    timerTurtle.hideturtle()
    timerTurtle.speed(0)
    timerTurtle.goto(-250, 250)
    scoringTurtle.penup()
    scoringTurtle.hideturtle()
    scoringTurtle.speed(0)
    scoringTurtle.goto(-250, 200)
    scoringTurtle.write("Score: " + str(playerScore), font = ("Arial", 20, "normal"))
    turtles.clear()
    for i in range(numberOfTurtles):
        turtles.append(turtle.Turtle())
    for t in turtles:
        t2: turtle = t
        t2.speed(0)
        t2.penup()
        turtle.register_shape("CS11_Mole.gif")
        t2.shape("CS11_Mole.gif")
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
        screen.ontimer(clock, 1000)

def clicked(x,y):
    global playerScore
    xClickThreshold = 10
    yClickThreshold = 10
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
    screen.bye()

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

setup(4)
clock()
screen.onclick(clicked)
screen.mainloop()
writeScores(updateScores(playerScore, readScores()))
