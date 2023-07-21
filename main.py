import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race enter a colo:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race = False
# tim = Turtle(shape="turtle")
# tim.color("blue")
# tim.penup()
# tim.goto(-240, 0)
y_position = [-150, -100, -50, 0, 50, 100]
i = 0
all_turtles = []
for colo in colors:

    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colo)
    tim.sety(y_position[i])
    tim.setx(-230)
    all_turtles.append(tim)
    i += 1

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won {winning_color}")
            else:
                print(f"you lost ! {winning_color} won")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
