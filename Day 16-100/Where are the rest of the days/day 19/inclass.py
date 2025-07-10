from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(50)
def move_backwards():
    tim.backward(50)
def turn_left():
    new = tim.heading()+10
    tim.setheading(new)
def turn_right():
    new = tim.heading()-10
    tim.setheading(new)
def move_clockwise():
    tim.clockwise(40)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
clear()
screen.onkey(clear,"c")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.exitonclick()
