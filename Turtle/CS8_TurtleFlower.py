import math
import turtle

t = turtle.Turtle()
s = turtle.Screen()
circleRadius = 20
numberOfPedals = 18
stemWidth = 30

s.bgcolor("light blue")
t.penup()
t.home()
t.setheading(180)
t.speed(0)
for i in range(numberOfPedals):
    color = "purple"
    if i % 2 == 1:
        color = "pink"
    t.dot(2*circleRadius, color)
    t.right(360/numberOfPedals)
    t.forward(2*circleRadius)
t.setheading(270)
for i in range(50):  
    t.dot(stemWidth, "#3ea832")
    t.forward(5)
t.goto((stemWidth)/math.sqrt(2), -100)
t.setheading(225)
t.dot(stemWidth, "#3ea832")
t.hideturtle()
s.mainloop()
