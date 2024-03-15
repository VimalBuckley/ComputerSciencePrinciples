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
        self.shown = False
        self.turt = turtle.Turtle(visible=False)
        self.turt.penup()
        self.turt.speed(0)
        self.turt.shape("square")
        self.turt.color("black")
        self.turt.shapesize(6, 6, 1)
        self.turt.goto(column * 120, -row * 120)
        self.turt.showturtle()
    
    def check(self):
        pass

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
screen.mainloop()