import turtle
import random
import os

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
    for t in turtles:
        t2: turtle = t
        t2.goto(random.choice(locations))
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
    for t in turtles:
        t2: turtle = t
        t2.hideturtle()
        t2.goto(1000,1000)
    timerTurtle.clear()
    timerTurtle.home()
    timerTurtle.write("Game Over", font = ("Arial", 20, "normal"))
        

def dealWithScoring():
    global playerName
    global playerScore
    nameList = []
    scoreList = []
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
    info.close()
    for i in range(len(scoreList)):
        if int(scoreList[i]) < int(playerScore) and not foundPlace:
            newNameList.append(playerName)
            newScoreList.append(playerScore)
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
dealWithScoring()