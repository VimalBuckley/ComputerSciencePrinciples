import turtle
import math
import random
import os
os.system("cls")
myScreen = turtle.Screen()
myScreen.screensize(500, 500)
setupTurtle = turtle.Turtle()
setupTurtle.hideturtle()
setupTurtle.speed(0)
setupTurtle.penup()
setupTurtle.goto(0, -250)
setupTurtle.color("red")
setupTurtle.pendown()
setupTurtle.begin_fill()
setupTurtle.circle(250)
setupTurtle.end_fill()
print(myScreen.screensize())

class clickTarget():
    def __init__(self):
        self.locations = [(250, 0, -180), (0, 250, 270), (-250, 0, 0), (0, -250, 90)]
        self.turtle1 = turtle.Turtle()
        self.turtle1.hideturtle()
        self.turtle1.speed(0)
        self.turtle1.penup()

        self.turtle2 = turtle.Turtle()
        self.turtle2.hideturtle()
        self.turtle2.speed(0)
        self.turtle2.penup()
    
    def loadTurtles(self):
        self.turtle1.hideturtle()
        self.turtle2.hideturtle()
        locations = [(250, 0, -180), (0, 250, 270), (-250, 0, 0), (0, -250, 90)]
        choice = random.choice(locations)
        locations.remove(choice)
        self.turtle1.goto(choice[0], choice[1])
        self.turtle1.setheading(choice[2])
        choice2 = random.choice(locations)
        self.turtle2.goto(choice2[0], choice2[1])
        self.turtle2.setheading(choice2[2])
        self.turtle1.showturtle()
        self.turtle2.showturtle()
        locations.append(choice)

    def moveTurtles(self):
        self.turtle1.forward(5)
        self.turtle2.forward(5)
        myScreen.ontimer(self.moveTurtles, 5)
        
origin = (0,0)
globalTarget = clickTarget()
globalTarget.loadTurtles()
globalTarget.moveTurtles()

def makeTarget():
    globalTarget.loadTurtles()
    globalTarget.moveTurtles()

def checkForClick(x, y):
    clickNearOrigin = math.dist(origin, (x,y)) < 100
    turtlesNearOrigin = math.dist(origin, globalTarget.turtle1.pos()) < 100
    if clickNearOrigin and turtlesNearOrigin:
        print("clicked")
        del globalTarget
        globalTarget = clickTarget()
        makeTarget()
    else:
        print("missed")

myScreen.listen()
myScreen.onclick(checkForClick)
myScreen.mainloop()