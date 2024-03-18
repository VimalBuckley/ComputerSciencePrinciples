import turtle
from enum import Enum
import time

screen = turtle.Screen()
player = turtle.Turtle()
playerColumn = 0
playerRow = 0
mazeHeight = 0
mazeWidth = 0
startTime = 0
walls = []
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
    [Tile.SPACE, Tile.SPACE, Tile.WALLL, Tile.SPACE, Tile.WALLL, Tile.SPACE, Tile.SPACE],
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
    
    def updateColor(self):
        # if not (
        #     playerRow + self.row < 0 or playerRow + self.row > mazeHeight or
        #     playerColumn + self.column < 0 or playerColumn + self.column > mazeWidth
        # ):
        if checkInbounds(playerRow + self.row, playerColumn + self.column):
            self.turt.color(maze[playerRow + self.row][playerColumn + self.column].value[1])
        else:
            self.turt.color("black")

def startGame():
    global walls
    global startTime
    checkMaze()
    screen.tracer(0, 0)
    screen.setup(600, 600)
    player.shape("square")
    player.shapesize(6, 6, 1)
    player.color("blue")
    player.penup()
    player.showturtle()
    walls = [Wall(row, column) for row in range(-2, 3) for column in range(-2, 3) if not (row == 0 and column == 0)]
    screen.onkeypress(lambda: move(-1, 0), "w")
    screen.onkeypress(lambda: move(1, 0), "s")
    screen.onkeypress(lambda: move(0, -1), "a")
    screen.onkeypress(lambda: move(0, 1), "d")
    screen.onkeypress(lambda: move(-1, 0), "Up")
    screen.onkeypress(lambda: move(1, 0), "Down")
    screen.onkeypress(lambda: move(0, -1), "Left")
    screen.onkeypress(lambda: move(0, 1), "Right")
    screen.listen()
    move(0, 0)
    startTime = time.time()
    screen.mainloop()

def checkMaze():
    '''
    Makes sure that the maze fits all the criteria of being a maze, to minimize bugs during gameplay\n
    These include:\n
    \t- All rows are the same length\n
    \t- There is exactly one start tile\n
    \t- There is at least one end tile\n
    '''
    
    global playerColumn
    global playerRow
    global mazeHeight
    global mazeWidth
    startFound = False
    endFound = False
    mazeHeight = len(maze) - 1
    for rowIndex in range(len(maze)):
        if rowIndex == 0:
            mazeWidth = len(maze[rowIndex]) - 1
        elif mazeWidth != len(maze[rowIndex]) - 1:
            raise Exception("Rows of differing length were found. Please note that all rows must be the same length!")
        for columnIndex in range(len(maze[rowIndex])):
            if maze[rowIndex][columnIndex] == Tile.START:
                if startFound:
                    raise Exception("Multiple start tiles were found. Please include exactly one start tile!")
                else:
                    playerColumn = columnIndex
                    playerRow = rowIndex
                    startFound = True
            elif maze[rowIndex][columnIndex] == Tile.ENDDD:
                endFound = True
    if not endFound:
        raise Exception("No end tiles were found. Please include at least one end tile!")

def checkInbounds(row: int, column: int):
    return not(row < 0 or row > mazeHeight or column < 0 or column > mazeWidth)

def end():
    print("You won!")
    print("Your time was:", str(time.time() - startTime), "seconds!")

def move(deltaRow: int, deltaColumn: int):
    global playerRow
    global playerColumn
    if checkInbounds(playerRow + deltaRow, playerColumn + deltaColumn):
        nextTile = maze[playerRow + deltaRow][playerColumn + deltaColumn]
        if nextTile == Tile.WALLL:
            pass
        elif nextTile == Tile.SPACE or nextTile == Tile.START:
            playerRow += deltaRow
            playerColumn += deltaColumn
            for wall in walls:
                wall.updateColor()
            screen.update()
        elif nextTile == Tile.ENDDD:
            playerRow += deltaRow
            playerColumn += deltaColumn
            screen.bye()
            end()

startGame()