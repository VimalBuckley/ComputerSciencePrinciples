import turtle

screen = turtle.Screen()
player = turtle.Turtle()
walls = []
class Wall:
    def __init__(self, column: int, row: int):
        self.column = column
        self.row = row
        sprite = turtle.Turtle()
        sprite.color("black")
        sprite.shape("square")
        sprite.shapesize(6, 6, 1)
        sprite.speed(0)
        sprite.penup()
        sprite.goto(getPos(column, row))

    def getPos(self):
        return (self.column, self.row)

def setupScreen():
    screen.setup(600, 600)
    screen.title("hi")

def setupPlayer():
    player.showturtle()
    player.color("red")
    player.shape("square")
    player.shapesize(6,6,1)
    player.penup()
    player.speed(0)

def getPos(column: int, row: int):
    xCoords = [-240, -120, 0, 120, 240]
    yCoords = [-240, -120, 0, 120, 240]
    if (column > 5):
        column = 5
    if (row > 5):
        row = 5
    if (column < 1) :
        column = 1
    if (row < 1):
        row = 1
    return xCoords[column - 1], yCoords[row - 1]

def movePlayer(column: int, row: int):
    '''
    column: which column (from 1 to 5) to move to \n 
    row: which row (from 1 to 5) to move to \n
    column 1 row 1 is the bottom left corner
    '''
    
    for w in walls:
        wall: Wall = w
        if (wall.getPos()[0] == column and wall.getPos()[1] == row):
            return
    player.goto(getPos(column, row))

def getPlayerPos():
    column = ((player.pos()[0] + 360) / 120) % 5
    row = ((player.pos()[1] + 360) / 120) % 5
    if (column == 0):
        column = 5
    if (row == 0):
        row = 5
    return (int(column), int(row)) 

setupScreen()
setupPlayer()
screen.listen()
screen.onkeypress(lambda :movePlayer(getPlayerPos()[0], getPlayerPos()[1] + 1), "w")
screen.onkeypress(lambda :movePlayer(getPlayerPos()[0] - 1, getPlayerPos()[1]), "a")
screen.onkeypress(lambda :movePlayer(getPlayerPos()[0], getPlayerPos()[1] - 1), "s")
screen.onkeypress(lambda :movePlayer(getPlayerPos()[0] + 1, getPlayerPos()[1]), "d")
walls.append(Wall(4, 4))
screen.mainloop()