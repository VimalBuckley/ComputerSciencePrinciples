import turtle
import math
import random
from enum import Enum
import os
import tkinter
tkinter.Frame()
os.system("cls")
myScreen = turtle.Screen()
myScreen.screensize(500, 500)
myScreen.title("Game")
turtles = []
startingDistance = 400

class Lane(Enum):
    RIGHT = ((startingDistance, 0), 180, "pink")
    UP = ((0, startingDistance), 270, "purple")
    LEFT = ((-startingDistance, 0), 0, "pink")
    DOWN = ((0, -startingDistance), 90, "purple")

class NoteReqs():
    def __init__(self, lane: Lane, timeMilliseconds: int):
        self.lane = lane
        self.time = timeMilliseconds

class CustomTurtle():
    def __init__(self, lane: Lane, customChart: bool, speed: int):
        self.lane = lane
        self.customChart = customChart
        self.myTurtle = turtle.Turtle()
        self.myTurtle.hideturtle()
        self.myTurtle.speed(0)
        self.myTurtle.penup()
        self.myTurtle.goto(self.lane.value[0])
        self.myTurtle.setheading(self.lane.value[1])
        self.myTurtle.shape("square")
        self.myTurtle.color(self.lane.value[2])
        self.myTurtle.showturtle()

    def moveForward(self, speed: int):
        self.myTurtle.forward(speed)

    def distanceFromStart(self):
        return math.dist(self.lane.value[0], self.myTurtle.pos())
    
    def isDone(self):
        if self.distanceFromStart() > 400:
            self.end()
            global maxScore
            maxScore += 4
            return True
        return False

    def end(self):
        self.myTurtle.hideturtle()
        if not self.customChart:
            createRandomNoteNow()
        del(self)

def moveTurtles(speed: int):
    for t in turtles:
        t2: CustomTurtle = t
        t2.moveForward(speed)
        if (t2.isDone()):
            turtles.pop(0)

def handleInputs(
    fullAccRange: int,
    halfAccRange: int,
    quarterAccRange: int,
    keysPressed: list,
    score: int,
    maxScore: int
):
    for t in turtles:
        note :CustomTurtle = t
        dist = startingDistance - note.distanceFromStart()
        if note.lane not in keysPressed or dist > quarterAccRange:
            continue
        if dist < fullAccRange:
            score += 4
        elif dist < halfAccRange:
            score += 2
        elif dist <= quarterAccRange:
            score += 1
        maxScore += 4
        note.end()
        turtles.remove(t)
    return score, maxScore

def handleAccuracy(scoringTurtle: turtle):
    global accuarcy
    global oldAccuracy
    if (maxScore != 0):
        accuarcy = score / maxScore
    if (accuarcy != oldAccuracy):
        scoringTurtle.clear()
        scoringTurtle.write(arg = "Accuracy: " + str(round(accuarcy * 100, 2)) + "%", font = ("Arial", 20, "normal"))
        oldAccuracy = accuarcy

def createNotes(notes: list = [(Lane.RIGHT, 0)]):
    for possibleNote in notes:
        createNote(possibleNote)

def createNote(note: tuple):
    myScreen.ontimer(lambda : turtles.append(CustomTurtle(note[0])), note[1])

def createRandomNoteNow():
    lanes = [Lane.UP, Lane.LEFT, Lane.DOWN, Lane.RIGHT]
    createNote((random.choice(lanes), 0))

def getPressedKeys(upKey: str, downKey: str, leftKey: str, rightKey: str):
    keysPressed = []
    myScreen.onkeypress(lambda : keysPressed.add(Lane.UP), upKey)
    myScreen.onkeypress(lambda : keysPressed.add(Lane.DOWN), downKey)
    myScreen.onkeypress(lambda : keysPressed.add(Lane.LEFT), leftKey)
    myScreen.onkeypress(lambda : keysPressed.add(Lane.RIGHT), rightKey)
    return keysPressed

def gameLoop(
    speed: int,
    fullAccRange: int,
    halfAccRange: int,
    quarterAccRange: int,
    scoringTurtle: turtle,
    score: int,
    maxScore: int
):
    moveTurtles(speed)
    score, maxScore = handleInputs(fullAccRange, halfAccRange, quarterAccRange, getPressedKeys(), score, maxScore)
    handleAccuracy(scoringTurtle)
    myScreen.ontimer(lambda: gameLoop(
        speed,
        fullAccRange, 
        halfAccRange, 
        quarterAccRange, 
        scoringTurtle,
        score,
        maxScore
    ), 10)

def drawBackground(
    fullAccRange: int,
    halfAccRange: int,
    quarterAccRange: int
):
    setupTurtle = turtle.Turtle()
    setupTurtle.hideturtle()
    setupTurtle.speed(0)
    setupTurtle.penup()
    setupTurtle.dot(quarterAccRange, "yellow")
    setupTurtle.dot(halfAccRange, "green")
    setupTurtle.dot(fullAccRange, "blue")
    del(setupTurtle)

def setupScoring():
    scoringTurtle = turtle.Turtle()
    scoringTurtle.hideturtle()
    scoringTurtle.speed(0)
    scoringTurtle.penup()
    scoringTurtle.goto(-200, 200)
    return scoringTurtle

def setup(
    upKey: str = "w", 
    downKey: str = "s", 
    leftKey: str = "a", 
    rightKey: str = "d", 
    customChart: bool = False,
    speed: int = 10,
    fullAccRange: int = 20,
    halfAccRange: int = 50,
    quarterAccRange: int = 100
):
    drawBackground(fullAccRange, halfAccRange, quarterAccRange)
    if customChart:
        createNotes([
            (Lane.RIGHT, 0),
            (Lane.UP, 100)
        ])
    else:
        createRandomNoteNow()
    myScreen.listen()
    gameLoop(speed, fullAccRange, halfAccRange, quarterAccRange, setupScoring())
    myScreen.mainloop()

setup()