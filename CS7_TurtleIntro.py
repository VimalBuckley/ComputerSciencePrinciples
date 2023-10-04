import turtle
import math

myScreen = turtle.Screen()

myScreen.bgcolor("red")
print(myScreen.screensize())
myTurtle = turtle.Turtle()
myTurtle.hideturtle()
myTurtle.speed(0)
myTurtle.color("blue", "green")

myTurtle.begin_fill()
myTurtle.forward(50)
for i in range(3):
    myTurtle.left(90)
    myTurtle.forward(50)
myTurtle.end_fill()

myTurtle.right(180)
myTurtle.forward(50)

myTurtle.color("blue", "black")
myTurtle.begin_fill()
myTurtle.right(45)
myTurtle.forward(25 * math.sqrt(2))
myTurtle.right(90)
myTurtle.forward(25 * math.sqrt(2))
myTurtle.end_fill()
myTurtle.ondrag(myTurtle.goto)
myTurtle.showturtle()
turtle.mainloop()