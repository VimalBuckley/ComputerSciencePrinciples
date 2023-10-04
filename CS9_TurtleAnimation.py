import turtle
import time

t = turtle.Turtle()
t2 = turtle.Turtle()
s = turtle.Screen()

s.bgpic("TestPeter.gif")
s.screensize(1366, 768)
xCoord = -200
t2.hideturtle()
t2.penup()
t2.speed(0)
t2.goto((-299, 100))
t2.write("Don't Let Peter Be Sad", font= ('Arial', 40, 'normal'))
while(True):
    t.clear()
    t.hideturtle()
    t.penup()
    t.speed(0)
    t.goto((-299, 100))
    t.write("Don't Let Peter Be Sad", font= ('Arial', 40, 'normal'))
    t.goto(xCoord, -50)
    t.write("Join Robotics Today!", ('Arial', 50, 'normal'))
    xCoord += 1
turtle.mainloop()

