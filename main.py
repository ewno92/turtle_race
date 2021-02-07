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

# draw the finish line
finish_line = turtle.Turtle()
finish_line.speed(0)
finish_line.penup()
finish_line.goto(230, 200)
finish_line.pendown()
finish_line.goto(230, -200)


user_bet = screen.textinput(
    title="make your bet", prompt="Which turtle will win the race? Enter a color: ")


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in racers:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle is the winner")
            else:
                print(f"You've lost! {winning_color} turtle is the winner")
            is_race_on = False
        rand_distance = random.randint(1, 30)
        turtle.forward(rand_distance)

screen.exitonclick()
