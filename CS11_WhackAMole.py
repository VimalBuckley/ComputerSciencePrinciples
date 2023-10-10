import turtle
import random

s = turtle.Screen()
s.bgcolor("red")
def randomizeTurtleLocations():
    for t in turtles:
        t.goto(random.choice(locations))
locations = [(-200, 150), (0, 150), (200, 150), (-200, 0), (0,0), (200, 0), (-200, -150), (0, -150), (200, -150)]
turtles = []
for i in range(4):
    turtles.append(turtle.Turtle())
for t in turtles:
    t.speed(0)
    t.penup()
    t.onclick(print())
randomizeTurtleLocations()



s.mainloop()