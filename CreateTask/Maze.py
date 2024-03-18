import turtle
from enum import Enum
import time

class Tile(Enum):
    SPACE = (False, "white")
    WALLL = (True, "black")
    ENDDD = (False, "red")
    START = (False, "green")

maze = [
    [Tile.SPACE, Tile.SPACE, Tile.SPACE, Tile.SPACE, Tile.SPACE, Tile.SPACE, Tile.SPACE],
    [Tile.SPACE, Tile.SPACE, Tile.ENDDD, Tile.WALLL, Tile.WALLL, Tile.SPACE, Tile.SPACE], 
    [Tile.SPACE, Tile.WALLL, Tile.SPACE, Tile.SPACE, Tile.SPACE, Tile.WALLL, Tile.SPACE], 
    [Tile.SPACE, Tile.WALLL, Tile.SPACE, Tile.START, Tile.SPACE, Tile.WALLL, Tile.SPACE], 
    [Tile.SPACE, Tile.WALLL, Tile.SPACE, Tile.SPACE, Tile.SPACE, Tile.WALLL, Tile.SPACE], 
    [Tile.SPACE, Tile.SPACE, Tile.WALLL, Tile.WALLL, Tile.WALLL, Tile.SPACE, Tile.SPACE],
    [Tile.SPACE, Tile.SPACE, Tile.SPACE, Tile.SPACE, Tile.SPACE, Tile.SPACE, Tile.SPACE]
]

class Wall:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.turt = turtle.Turtle()
        self.turt.penup()
        self.turt.speed(0)
        self.turt.shape("square")
        self.turt.color("black")
        self.turt.shapesize(6, 6, 1)
        self.turt.goto(column * 120, -row * 120)
        self.turt.showturtle()
    
    def check(self):
        try:
            self.turt.color(maze[playerRow + self.row][playerColumn + self.column].value[1])
        except:
            self.turt.color("white")
screen = turtle.Screen()
screen.tracer(0, 0)
screen.setup(600, 600)
player = turtle.Turtle()
player.shape("square")
player.shapesize(6, 6, 1)
player.color("blue")
player.penup()
player.showturtle()
playerColumn = 0
playerRow = 0
startFound = False
for rowIndex in range(len(maze)):
    for columnIndex in range(len(maze[rowIndex])):
        if maze[rowIndex][columnIndex] == Tile.START:
            playerColumn = columnIndex
            playerRow = rowIndex
            if startFound == True:
                raise Exception("Multiple starts were found in the maze. Please make sure to provide exactly one start tile!")
            startFound = True
if not startFound:
    raise Exception("The start of the maze coulnd't be found. Please make sure a start tile was provided!")
startTime = 0

walls = [Wall(row, column) for row in range(-2, 3) for column in range(-2, 3) if not (row == 0 and column == 0)]
def end():
    print("You won!")
    print("Your time was:", str(time.time() - startTime), "seconds!")
def move(deltaRow: int, deltaColumn: int):
    global playerRow
    global playerColumn
    nextTile = maze[playerRow + deltaRow][playerColumn + deltaColumn]
    if nextTile == Tile.WALLL:
        pass
    elif nextTile == Tile.SPACE or nextTile == Tile.START:
        playerRow += deltaRow
        playerColumn += deltaColumn
        for wall in walls:
            wall.check()
        screen.update()
    elif nextTile == Tile.ENDDD:
        playerRow += deltaRow
        playerColumn += deltaColumn
        screen.bye()
        end()
screen.onkeypress(lambda: move(-1, 0), "w")
screen.onkeypress(lambda: move(1, 0), "s")
screen.onkeypress(lambda: move(0, -1), "a")
screen.onkeypress(lambda: move(0, 1), "d")
screen.onkeypress(lambda: move(-1, 0), "Up")
screen.onkeypress(lambda: move(1, 0), "Down")
screen.onkeypress(lambda: move(0, -1), "Left")
screen.onkeypress(lambda: move(0, 1), "Right")
screen.listen()
startTime = time.time()
move(0, 0)
screen.mainloop()