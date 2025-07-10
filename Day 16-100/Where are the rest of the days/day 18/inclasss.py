from turtle import Turtle , Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("pink")
timmy.forward(100)
timmy.backward(200)
timmy.right(90)
#question 1
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

#question 2
for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

#question3
tim = Turtle()
tim.shape("turtle")
tim.width(2)
tim.speed("fastest")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "brown","DarkSeaGreen"]

def draw_polygon(sides, length):
    angle = 360 / sides
    tim.color(random.choice(colors))
    for _ in range(sides):
        tim.forward(length)
        tim.right(angle)

for num_sides in range(3, 11):
    draw_polygon(num_sides, 100)


#question4
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "brown","DarkSeaGreen","CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]
timmy.pensize(10)
timmy.speed("fastest")
for _ in range(400):
    timmy.color(random.choice(colors))
    timmy.forward(25)
    timmy.setheading(random.choice(directions))

timmy.speed("fastest")
screen = Screen()
screen.bgcolor("pink")

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

screen.colormode(1.0)

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)

draw_spirograph(5)



screen.exitonclick()