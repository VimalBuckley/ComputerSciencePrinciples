import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()
s = turtle.Screen()
count = 1
xPose = 0
doneOnce = False

s.bgpic("CS9_Peter.gif")
s.screensize(1366, 768)
xCoord = -200
turtle.register_shape("CS9_JoinRobotics.gif")
t.shape("CS9_JoinRobotics.gif")
t.resizemode("user")
t.speed(0)
t.penup()
t.goto(0, -50)
t2.hideturtle()
t2.penup()
t2.speed(0)
t2.goto((-250, 100))
t2.write("Don't Let Peter Be Sad", font= ('Arial', 40, 'normal'))
while True:
    t.forward(5)
    if t.pos()[0] >= s.screensize()[0] / 2:
        count += 1
        t.goto(-s.screensize()[0] / 2, -50)
        t2.goto(-14, 180)
        t2.dot(count * 5, "red")
        t2.goto(215, 163)
        t2.dot(count * 5, "red")

