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
customChart = True
oldAccuracy = accuarcy
myScreen = turtle.Screen()
myScreen.screensize(500, 500)
myScreen.title("Game")
myTurtle = turtle.Turtle()
myTurtle.hideturtle()
myTurtle.speed(0)
myTurtle.penup()
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
    RIGHT = (lambda currentDistance : (currentDistance - speed, 0), "red")
    UP = (lambda currentDistance : (0, currentDistance - speed), "black")
    LEFT = (lambda currentDistance : (-(currentDistance - speed), 0), "red")
    DOWN = (lambda currentDistance : (0, -(currentDistance - speed)), "black")

class Note():
    def __init__(self, lane: Lane):
        self.lane = lane
        self.distance = 400
    
    def getNextPose(self):
        return self.lane.value[0](self.distance)
    
    def isDone(self):
        if self.distance > quarterAccuracyRange or self.lane not in keysPressed:
            return False
        if 


notes = [
    Note(Lane.RIGHT),
    Note(Lane.UP)
]

def drawNotes():
    myTurtle.clear()
    for note in notes:
        myTurtle.goto(note.getNextPose())
        myTurtle.dot(10, note.lane.value[1])
        note.distance = math.dist(myTurtle.pos(), (0,0))

for i in range(10):
    drawNotes()

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