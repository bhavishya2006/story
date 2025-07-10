# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(50)
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()

import turtle
from turtle import Turtle, Screen
import random


def turtle_racing():
    colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange']
    start_y_positions = [-200, -150, -100, -50, 0, 50]

    turtles = []
    for color, y in zip(colors, start_y_positions):
        t = Turtle()
        t.shape('turtle')
        t.color(color)
        t.penup()
        t.goto(-225, y)
        t.speed(1)
        turtles.append(t)

    screen = Screen()
    player_choice = screen.textinput("BET", "Who will win? Blue, Red, Green, Yellow, Purple, or Orange? ").lower()

    race_is_on = True
    while race_is_on:
        for t in turtles:
            t.forward(random.randint(1, 20))
            if t.xcor() > 350:
                winner = t.pencolor()  # get turtle color
                print(f"{winner.capitalize()} won!")
                if player_choice == winner:
                    print("You bet on the right color, congratulations!")
                else:
                    print("You bet on the wrong color")
                race_is_on = False
                break

def reset():
    screen.clear()
    turtle_racing()

screen = Screen()
screen.listen()
screen.onkey(reset, "c")
turtle_racing()
screen.exitonclick()
