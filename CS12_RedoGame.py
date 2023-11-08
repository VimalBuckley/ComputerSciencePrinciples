from enum import Enum
import turtle
import math
import random

keys_pressed: set = set()

class Lane(Enum):
    RIGHT = ((400, 0), 180, "pink")
    UP = ((0, 400), 270, "purple")
    LEFT = ((-400, 0), 0, "pink")
    DOWN = ((0, -400), 90, "purple")

class Note():
    def __init__(self, lane: Lane, speed: int, newNoteOnClick: bool):
        self.lane = lane
        self.speed = speed
        self.newNoteOnClick = newNoteOnClick
        self.my_turtle = turtle.Turtle()
        self.my_turtle.hideturtle()
        self.my_turtle.speed(0)
        self.my_turtle.penup()
        self.my_turtle.goto(lane.value[0])
        self.my_turtle.setheading(self.lane.value[1])
        self.my_turtle.shape("square")
        self.my_turtle.color(self.lane.value[2])
        self.my_turtle.showturtle()

    def move_forward(self):
        self.my_turtle.forward(self.speed)

    def distance_from_start(self):
        return math.dist(self.lane.value[0], self.my_turtle.pos())

    def check_if_end(self, note_list: list):
        if self.distance_from_start() > 400:
            self.end(note_list)
            return 4
        return 0
    
    def end(self, note_list: list):
        self.my_turtle.hideturtle()
        note_list.remove(self)
        if self.newNoteOnClick:
            start_note_chain(note_list, self.speed)

def start_note_chain(note_list: list, speed: int):
    note_list.append(Note(random.choice(list(Lane)), speed, True))

def assign_keybinds(
    screen: turtle._Screen,
    up_key: str,
    left_key: str,
    down_key: str,
    right_key: str
):
    screen.listen()
    screen.onkeypress(lambda: keys_pressed.add("up"), up_key)
    screen.onkeypress(lambda: keys_pressed.add("left"), left_key)
    screen.onkeypress(lambda: keys_pressed.add("down"), down_key)
    screen.onkeypress(lambda: keys_pressed.add("right"), right_key)
    screen.onkey(lambda: keys_pressed.discard("up"), up_key)
    screen.onkey(lambda: keys_pressed.discard("left"), left_key)
    screen.onkey(lambda: keys_pressed.discard("down"), down_key)
    screen.onkey(lambda: keys_pressed.discard("right"), right_key)

def draw_ranges(
    fullAccRange: int,
    halfAccRange: int,
    quarterAccRange: int
):
    drawing_turtle = turtle.Turtle()
    drawing_turtle.hideturtle()
    drawing_turtle.speed(0)
    drawing_turtle.penup()
    drawing_turtle.home()
    drawing_turtle.dot(quarterAccRange, "yellow")
    drawing_turtle.dot(halfAccRange, "green")
    drawing_turtle.dot(fullAccRange, "blue")
    del drawing_turtle

def handle_inputs(
    note_list: list,
    full_acc_range: int,
    half_acc_range: int,
    quarter_acc_range: int
):
    for note in note_list:
        

def game_loop(
    screen: turtle._Screen, 
    note_list: list, 
    full_acc_range: int, 
    half_acc_range: int, 
    quarter_acc_range: int,
    score: int,
    max_score: int
):
    for note in note_list:
        note.move_forward()
        max_score += note.check_if_end(note_list)
    screen.ontimer(
        lambda: game_loop(
            screen, 
            note_list, 
            full_acc_range, 
            half_acc_range, 
            quarter_acc_range,
            score,
            max_score
        ),
        10
    )
    
def setup(
    up_key: str = "w",
    left_key: str = "a",
    down_key: str = "s",
    right_key: str = "d",
    do_custom_chart: bool = False,
    speed: int = 10,
    full_acc_range: int = 20,
    half_acc_range: int = 50,
    quarter_acc_range: int = 100
):
    my_screen = turtle.Screen()
    my_screen.screensize(500, 500)
    note_list = []
    assign_keybinds(
        my_screen,
        up_key,
        left_key,
        down_key,
        right_key
    )
    draw_ranges(
        full_acc_range,
        half_acc_range,
        quarter_acc_range
    )
    if not do_custom_chart:
        start_note_chain(note_list, speed)
    game_loop(my_screen, note_list)
    my_screen.mainloop()

setup() 