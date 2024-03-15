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
            print("yes")
            self.turt.showturtle()
        else:
            print("no")
            self.turt.hideturtle()


screen = turtle.Screen()
screen.setup(600, 600)
walls = [
    Wall(-2, -2),
    Wall(-2, -1),
    Wall(-2, 0),
    Wall(-2, 1),
    Wall(-2, 2),
    Wall(-1, -2),
    Wall(-1, -1),
    Wall(-1, 0),
    Wall(-1, 1),
    Wall(-1, 2),
    Wall(0, -2),
    Wall(0, -1),
    Wall(0, 1),
    Wall(0, 2),
    Wall(1, -2),
    Wall(1, -1),
    Wall(1, 0),
    Wall(1, 1),
    Wall(1, 2),
    Wall(2, -2),
    Wall(2, -1),
    Wall(2, 0),
    Wall(2, 1),
    Wall(2, 2)
]
player = turtle.Turtle(visible=False)
player.shape("square")
player.shapesize(6, 6, 1)
player.color("red")
player.penup()
player.showturtle()
playerColumn = 3
playerRow = 3
for wall in walls:
    wall.check()

def up():
    playerRow - 1
    print(playerRow)
    for wall in walls:
        wall.check()
def down():
    playerRow + 1
    print(playerRow)
    for wall in walls:
        wall.check()
def right():
    playerColumn + 1
    print(playerColumn)
    for wall in walls:
        wall.check()
def left():
    playerColumn - 1
    print(playerColumn)
    for wall in walls:
        wall.check()

screen.onkeypress(lambda: up(), "w")
screen.onkeypress(lambda: down(), "s")
screen.onkeypress(lambda: left(), "a")
screen.onkeypress(lambda: right(), "d")
screen.listen()
screen.mainloop()