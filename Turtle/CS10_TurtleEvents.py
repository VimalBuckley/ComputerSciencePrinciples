import turtle
import math

s = turtle.Screen()
t = turtle.Turtle()
t.home()
t.penup()
t.speed(0)
loopsPerSecond = 10000
isRunning = True
velocity = (0,0)

def moveRight():
    global velocity
    velocity = (1, velocity[1])
def moveLeft():
    global velocity
    velocity = (-1, velocity[1])
def moveUp():
    global velocity
    velocity = (velocity[0], 1)
def moveDown():
    global velocity
    velocity = (velocity[0], -1)
def zeroSidewaysVelocity():
    global velocity
    velocity = (0, velocity[1])
def zeroForwardVelocity():
    global velocity
    velocity = (velocity[0], 0)
def stopMoving():
    zeroForwardVelocity()
    zeroSidewaysVelocity()
def gameLoop():
    if velocity[0] != 0:
        t.setheading(math.atan(velocity[1]/velocity[0]))
    elif velocity[1] >= 0:
        t.setheading(0)
    else: 
        t.setheading(180)
    t.forward(math.dist((0,0), velocity))
    s.onkeypress(moveUp, "Up")
    s.onkeypress(moveDown, "Down")
    s.onkeypress(moveRight, "Right")
    s.onkeypress(moveLeft, "Left")
    s.onkeypress(zeroSidewaysVelocity, "Left")
    s.onkeypress(zeroSidewaysVelocity, "Right")
    s.onkeypress(zeroForwardVelocity, "Up")
    s.onkeypress(zeroForwardVelocity, "Down")
    s.onkey(stopMoving, "a")
    # s.onkeyrelease(stopMoving, "Space")
    s.ontimer(gameLoop, int(1000/loopsPerSecond))

# s.onkeypress(moveRight, "Right")
gameLoop()
s.listen()
s.mainloop()