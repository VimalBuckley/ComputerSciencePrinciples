import turtle
walls = []
class Wall:

    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.turt = turtle.Turtle()
        self.turt.hideturtle()
        self.turt.penup()
        self.turt.shape("square")
        self.turt.color("black")
        self.turt.speed(0)
        self.turt.shapesize(6, 6, 1)
        self.turt.goto(row, column)
        
    def update(self, playerRow: int, playerColumn: int):
        if abs(self.row - playerRow) <= 2 and abs(self.column - playerColumn):
            self.turt
    

    

screen = turtle.Screen()
player = turtle.Turtle()
myWall = Wall(120, 120)
screen.setup(600, 600)
player.shape("square")
player.shapesize(6, 6, 1)
player.color("red")
player.penup()
player.showturtle()
screen.mainloop()