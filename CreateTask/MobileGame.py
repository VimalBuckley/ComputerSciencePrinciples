import turtle
import math
import time

screen = turtle.Screen()
player = turtle.Turtle()

def setupScreen():
    screen.bgpic("CreateTask/Bigger Checker Board.png")
    screen.setup(600, 600)
    screen.title("hi")

def setupPlayer():
    player.showturtle()
    player.color("red")
    player.shape("square")
    player.shapesize(6,6,1)
    player.penup()
    player.speed(0)

def movePlayer(column: int, row: int):
    '''
    column: which column (from 1 to 5) to move to \n 
    row: which row (from 1 to 5) to move to \n
    column 1 row 1 is the bottom left corner
    '''
    xCoords = [-240, -120, 0, 120, 240]
    yCoords = [-240, -120, 0, 120, 240]
    if (column > 5):
        column = 0
    player.goto(xCoords[column - 1], yCoords[row - 1])

def getPlayerPos():
    column = ((player.pos()[0] + 360) / 120) % 5
    row = ((player.pos()[1] + 360) / 120) % 5
    return (column, row) 

setupScreen()
setupPlayer()
while True:
    column = int(screen.numinput("Question", "What column?"))
    row = int(screen.numinput("Question", "What row?"))
    movePlayer(column, row)
    print(getPlayerPos())
    print(player.pos())

turtle.mainloop()