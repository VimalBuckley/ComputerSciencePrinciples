from enum import Enum
import turtle
import math
import random

class Lane(Enum):
    RIGHT = ((400, 0), 180, "pink")
    UP = ((0, 400), 270, "purple")
    LEFT = ((-400, 0), 0, "pink")
    DOWN = ((0, -400), 90, "purple")

class Note():
    def __init__(self, lane: Lane = Lane.RIGHT, speed: int = 10, newNoteOnClick: bool = False):
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

    def check_if_end(self, note_list: list, score: int, max_score: int, scoring_turtle: turtle.Turtle):
        if self.distance_from_start() > 400:
            self.end(note_list)
            max_score += 4
            draw_acc(scoring_turtle, score, max_score)
        max_score += 0
        return score, max_score
    
    def end(self, note_list: list):
        self.my_turtle.hideturtle()
        note_list.remove(self)
        if self.newNoteOnClick:
            start_note_chain(note_list, self.speed)

class CustomChartNote():
    def __init__(self, lane: Lane, speed: int, time: int):
        self.lane = lane
        self.speed = speed
        self.time = time

def make_note_at_time(screen: turtle._Screen,note_list: list, lane: Lane, speed: int, time: int):
    screen.ontimer(lambda: note_list.append(Note(lane, speed, False)), time)

def start_note_chain(note_list: list, speed: int):
    note_list.append(Note(random.choice(list(Lane)), speed, True))

def assign_keybinds(
    screen: turtle._Screen,
    keys_pressed: set,
    up_key: str,
    left_key: str,
    down_key: str,
    right_key: str
):
    screen.listen()
    screen.onkeypress(lambda: keys_pressed.add(Lane.UP), up_key)
    screen.onkeypress(lambda: keys_pressed.add(Lane.LEFT), left_key)
    screen.onkeypress(lambda: keys_pressed.add(Lane.DOWN), down_key)
    screen.onkeypress(lambda: keys_pressed.add(Lane.RIGHT), right_key)
    screen.onkey(lambda: keys_pressed.discard(Lane.UP), up_key)
    screen.onkey(lambda: keys_pressed.discard(Lane.LEFT), left_key)
    screen.onkey(lambda: keys_pressed.discard(Lane.DOWN), down_key)
    screen.onkey(lambda: keys_pressed.discard(Lane.RIGHT), right_key)

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
    drawing_turtle.dot(2 * quarterAccRange, "yellow")
    drawing_turtle.dot(2 * halfAccRange, "green")
    drawing_turtle.dot(2 * fullAccRange, "blue")
    del drawing_turtle

def draw_acc(
    scoring_turtle: turtle.Turtle,
    score: int = 0,
    max_score: int = 0
):
    scoring_turtle.hideturtle()
    scoring_turtle.speed(0)
    scoring_turtle.penup()
    scoring_turtle.goto(-200, 200)
    scoring_turtle.clear()
    acc = 100
    if max_score != 0:
        acc = round((100 * score / max_score), 2)
    scoring_turtle.write(arg = "Accuracy: " + str(acc) + "%", font = ("Arial", 20, "normal"))

def handle_inputs(
    note_list: list,
    keys_pressed: set,
    full_acc_range: int,
    half_acc_range: int,
    quarter_acc_range: int,
    score: int,
    max_score: int,
    scoring_turtle: turtle.Turtle
):
    for n in note_list:
        note: Note = n
        dist = 400 - note.distance_from_start()
        if dist > quarter_acc_range or note.lane not in keys_pressed:
            continue
        if dist < full_acc_range:
            score += 4
        elif dist < half_acc_range:
            score += 2
        elif dist <= quarter_acc_range:
            score += 1
        max_score += 4
        draw_acc(scoring_turtle, score, max_score)
        note.end(note_list)
    return score, max_score

def game_loop(
    screen: turtle._Screen, 
    keys_pressed: set, 
    full_acc_range: int, 
    half_acc_range: int, 
    quarter_acc_range: int,
    scoring_turtle: turtle.Turtle = turtle.Turtle(),
    note_list: list = [],
    score: int = 0,
    max_score: int = 0
):
    for n in note_list:
        note: Note = n
        note.move_forward()
        score, max_score = note.check_if_end(note_list, score, max_score, scoring_turtle)
    score, max_score = handle_inputs(
        note_list, 
        keys_pressed, 
        full_acc_range, 
        half_acc_range, 
        quarter_acc_range, 
        score, 
        max_score, 
        scoring_turtle
    )

    screen.ontimer(
        lambda: game_loop(
            screen,
            keys_pressed, 
            full_acc_range, 
            half_acc_range, 
            quarter_acc_range,
            scoring_turtle,
            note_list,
            score,
            max_score
        ),
        10
    )
    
def setup(
    custom_chart: list = None,
    up_key: str = "w",
    left_key: str = "a",
    down_key: str = "s",
    right_key: str = "d",
    speed: int = 10,
    full_acc_range: int = 20,
    half_acc_range: int = 50,
    quarter_acc_range: int = 100
):
    my_screen = turtle.Screen()
    my_screen.screensize(500, 500)
    note_list = []
    keys_pressed = set()
    assign_keybinds(
        my_screen,
        keys_pressed,
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
    if custom_chart is None:
        start_note_chain(note_list, speed)
    else:
        for n in custom_chart:
            custom_note: CustomChartNote = n
            make_note_at_time(my_screen, note_list, custom_note.lane, custom_note.speed, custom_note.time)
    game_loop(my_screen, keys_pressed, full_acc_range, half_acc_range, quarter_acc_range, note_list=note_list)
    my_screen.mainloop()

example_custom_chart = [
    CustomChartNote(Lane.RIGHT, 10, 1000),
    CustomChartNote(Lane.LEFT, 10, 500),
    CustomChartNote(Lane.DOWN, 10, 2000)
]

setup()