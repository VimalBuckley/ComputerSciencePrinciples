import turtle
import math
import os
os.system("cls")
myScreen = turtle.Screen()
myScreen.screensize(500, 500)
setupTurtle = turtle.Turtle()
setupTurtle.showturtle()
setupTurtle.speed(9)
setupTurtle.penup()
setupTurtle.goto(0, -250)
# setupTurtle.color("red")
# setupTurtle.pendown()
# setupTurtle.begin_fill()
# setupTurtle.circle(250)
setupTurtle.end_fill()
print(myScreen.screensize())

class clickTarget():
    def __init__(self, angles: tuple = (0,0), duration :float = 3):
        self.angles = angles
        self.duration = duration
        self.turtle1 = turtle.Turtle(False)
        self.turtle1.hideturtle()
        self.turtle1.speed(0)
        self.turtle1.penup()

        self.turtle2 = turtle.Turtle(False)
        self.turtle2.hideturtle()
        self.turtle2.speed(0)
        self.turtle2.penup()
    
    def loadTurtles(self):
        self.turtle1.goto()
        



myScreen.listen()
myScreen.mainloop()