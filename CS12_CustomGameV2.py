import turtle

size = 50
speed = 5
my_screen = turtle.Screen()
my_screen.screensize(650, 650)
my_screen.setup(700, 700)
my_screen.title("Game")

vertical_turtle = turtle.Turtle()
vertical_turtle.speed(0)
vertical_turtle.hideturtle()
vertical_turtle.penup()
vertical_turtle.goto(-325, 0)
vertical_turtle.showturtle()

horizontal_turtle = turtle.Turtle()
horizontal_turtle.speed(0)
horizontal_turtle.hideturtle()
horizontal_turtle.penup()
horizontal_turtle.goto(0, -325)
horizontal_turtle.showturtle()


def load_a_turtle(coordinate: tuple):
    temp_turtle = turtle.Turtle()
    temp_turtle.hideturtle()
    temp_turtle.speed(speed)
    temp_turtle.penup()
    temp_turtle.goto(coordinate)
    temp_turtle.pendown()
    temp_turtle.pencolor("red")
    temp_turtle.fillcolor("red")
    temp_turtle.begin_fill()
    temp_turtle.circle(size)
    temp_turtle.end_fill()

coordinates = [
    (0, 0)
]

my_screen.mainloop()