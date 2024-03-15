import turtle
maze = [
    [False, False, False, False, False, False, False],
    [False, False, True , True , True , False, False], 
    [False, True , False, False, False, True , False], 
    [False, True , False, False, False, True , False], 
    [False, True , False, False, False, True , False], 
    [False, False, True , True , True , False, False],
    [False, False, False, False, False, False, False]
]

class Wall:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.turt = turtle.Turtle(visible=False)
        self.turt.penup()
        self.turt.speed(0)
        self.turt.shape("square")
        self.turt.color("black")
        self.turt.shapesize(6, 6, 1)
        self.turt.goto(column * 120, -row * 120)
        self.turt.showturtle()
    
    def check(self):
        if (maze[playerRow + self.row][playerColumn + self.column]):
            self.turt.showturtle()
        else:
            self.turt.hideturtle()


screen = turtle.Screen()
screen.setup(600, 600)
player = turtle.Turtle(visible=False)
player.shape("square")
player.shapesize(6, 6, 1)
player.color("red")
player.penup()
player.showturtle()
playerColumn = 3
playerRow = 3
walls = [Wall(row, column) for row in range(-2, 3) for column in range(-2, 3) if not (row == 0 and column == 0)]
for wall in walls:
    wall.check()
def move(deltaRow: int, deltaColumn: int):
    global playerRow
    global playerColumn
    playerRow += deltaRow
    playerColumn += deltaColumn
    if (maze[playerRow][playerColumn]):
        playerRow -= deltaRow
        playerColumn -= deltaColumn
    for wall in walls:
        wall.check()

screen.onkeypress(lambda: move(-1, 0), "w")
screen.onkeypress(lambda: move(1, 0), "s")
screen.onkeypress(lambda: move(0, -1), "a")
screen.onkeypress(lambda: move(0, 1), "d")
screen.listen()
screen.mainloop()