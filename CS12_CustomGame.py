import turtle
import math
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
    def __init__(self, coordinate: tuple = (0,0), duration :float = 3):
        self.coordinate = coordinate
        self.duration = duration
        self.turtle1 = turtle.Turtle()
        self.turtle2 = turtle.Turtle()
    

        



myScreen.listen()
myScreen.mainloop()