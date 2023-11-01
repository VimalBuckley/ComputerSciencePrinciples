import turtle
import math
import random
from enum import Enum
import os
os.system("cls")
upKey = input("Choose your up keybind\n")
leftKey = input("Choose your left keybind\n")
downKey = input("Choose your down keybind\n")
rightKey = input("Choose your right keybind\n")
myScreen = turtle.Screen()
myScreen.screensize(500, 500)
turtles = []
keysPressed = {"test"}
keysPressed.discard("test")

class Lane(Enum):
    RIGHT = ((400, 0), 180)
    UP = ((0, 400), 270)
    LEFT = ((-400, 0), 0)
    DOWN = ((0, -400), 90)

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
        self.myTurtle.color("red")
        self.myTurtle.showturtle()

    def moveForward(self):
        self.myTurtle.forward(5)

    def distanceFromStart(self):
        return math.dist(self.lane.value[0], self.myTurtle.pos())
    
    def isDone(self):
        if self.distanceFromStart() > 400:
            self.end()
            return True
        return False

    def end(self):
        self.myTurtle.hideturtle()

def moveTurtles():
    for t in turtles:
        t2: CustomTurtle = t
        t2.moveForward()
        if (t2.isDone()):
            turtles.pop(0)

def gameLoop():
    moveTurtles()
    myScreen.ontimer(gameLoop, 1)

def testPrint():
    print("Hi")

def createNotes(notes: list = [NoteReqs(Lane.RIGHT, 0)]):
    for possibleNote in notes:
        createNote(possibleNote)

def createNote(note):
    myScreen.ontimer(lambda : turtles.append(CustomTurtle(note.lane)), note.time)

createNotes([])
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