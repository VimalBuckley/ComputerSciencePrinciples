import turtle
import math
import random
from enum import Enum
import os
os.system("cls")
upKey = "w"
leftKey = "a"
downKey = "s"
rightKey = "d"
speed = 10
score = 0
maxScore = 0
accuarcy = 1
customChart = False
oldAccuracy = accuarcy
myScreen = turtle.Screen()
myScreen.screensize(500, 500)
myScreen.title("Game")
turtles = []
keysPressed = set()
startingDistance = 400
fullAccuracyRange = 20
halfAccuracyRange = 50
quarterAccuracyRange = 100
scoringTurtle = turtle.Turtle()
scoringTurtle.hideturtle()
scoringTurtle.speed(0)
scoringTurtle.penup()
scoringTurtle.goto(-200, 200)
setupTurtle = turtle.Turtle()
setupTurtle.hideturtle()
setupTurtle.speed(0)
setupTurtle.penup()
setupTurtle.dot(quarterAccuracyRange, "yellow")
setupTurtle.dot(halfAccuracyRange, "green")
setupTurtle.dot(fullAccuracyRange, "blue")
del(setupTurtle)

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
    def __init__(self, lane: Lane):
        self.lane = lane
        self.myTurtle = turtle.Turtle()
        self.myTurtle.hideturtle()
        self.myTurtle.speed(0)
        self.myTurtle.penup()
        self.myTurtle.goto(self.lane.value[0])
        self.myTurtle.setheading(self.lane.value[1])
        self.myTurtle.shape("square")
        self.myTurtle.color(self.lane.value[2])
        self.myTurtle.showturtle()

    def moveForward(self):
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
        if not customChart:
            createRandomNoteNow()
        del(self)

def moveTurtles():
    for t in turtles:
        t2: CustomTurtle = t
        t2.moveForward()
        if (t2.isDone()):
            turtles.pop(0)

def handleInputs():
    global keysPressed
    global turtles
    global score
    global maxScore
    for t in turtles:
        note :CustomTurtle = t
        dist = startingDistance - note.distanceFromStart()
        if note.lane not in keysPressed or dist > quarterAccuracyRange:
            continue
        if dist < fullAccuracyRange:
            score += 4
        elif dist < halfAccuracyRange:
            score += 2
        elif dist <= quarterAccuracyRange:
            score += 1
        maxScore += 4
        note.end()
        turtles.remove(note)

def handleAccuracy():
    global accuarcy
    global oldAccuracy
    if (maxScore != 0):
        accuarcy = score / maxScore
    if (accuarcy != oldAccuracy):
        scoringTurtle.clear()
        scoringTurtle.write(arg = "Accuracy: " + str(round(accuarcy * 100, 2)) + "%", font = ("Arial", 20, "normal"))
        oldAccuracy = accuarcy

def gameLoop():
    moveTurtles()
    handleInputs()
    handleAccuracy()
    myScreen.ontimer(gameLoop, 10)

def testPrint():
    print("Hi")

def createNotes(notes: list = [(Lane.RIGHT, 0)]):
    for possibleNote in notes:
        createNote(possibleNote)

def createNote(note: tuple):
    myScreen.ontimer(lambda : turtles.append(CustomTurtle(note[0])), note[1])

def createRandomNoteNow():
    lanes = [Lane.UP, Lane.LEFT, Lane.DOWN, Lane.RIGHT]
    createNote((random.choice(lanes), 0))

if customChart:
    createNotes([
        (Lane.LEFT, 0),
        (Lane.RIGHT, 0),
        (Lane.UP, 324),
        (Lane.UP, 1256),
        (Lane.DOWN, 21)
    ])
else:
    createRandomNoteNow()
gameLoop()
myScreen.listen()
myScreen.onkeypress(lambda : keysPressed.add(Lane.UP), upKey)
myScreen.onkeypress(lambda : keysPressed.add(Lane.DOWN), downKey)
myScreen.onkeypress(lambda : keysPressed.add(Lane.LEFT), leftKey)
myScreen.onkeypress(lambda : keysPressed.add(Lane.RIGHT), rightKey)
myScreen.onkey(lambda : keysPressed.discard(Lane.UP), upKey)
myScreen.onkey(lambda : keysPressed.discard(Lane.DOWN), downKey)
myScreen.onkey(lambda : keysPressed.discard(Lane.LEFT), leftKey)
myScreen.onkey(lambda : keysPressed.discard(Lane.RIGHT), rightKey)
myScreen.mainloop()