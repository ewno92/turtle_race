import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(500, 400)
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [120, 60, 0, -60, -120, -180]
# “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
racers = []
for _ in range(0, 6):
    racer = turtle.Turtle("turtle")
    racer.speed(0)
    racers.append(racer)
    racer.color(color[_])
    racer.penup()
    racer.goto(-230, y_position[_])

user_bet = screen.textinput(
    title="make your bet", prompt="Which turtle will win the race? Enter a color: ")


if user_bet:
    is_race_on = True

while is_race_on:
    rand_distance = random.randint(1, 5)

    screen.exitonclick()
