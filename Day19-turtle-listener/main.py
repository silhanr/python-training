import random
from turtle import Turtle, Screen

#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.back(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.up()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)



colors = ["red", "green", "blue", "yellow", "orange", "purple"]

screen = Screen()
height = 400
width = 500
size = 20
screen.setup(width,height)
is_race_on = False

guess = screen.textinput("Winner?", "Who is gonna win?: ")

if guess:
    is_race_on = True

turtle_racers = []
for i in range(6):
    turtle_racers.append(Turtle(shape="turtle"))
    turtle_racers[i].color(colors[i])
    turtle_racers[i].penup()
    turtle_racers[i].goto(-width/2+20,-height/2+50+i*50)

winner = ""

while is_race_on:
    for turtle in turtle_racers:
        if turtle.xcor() > width/2 - size:
            is_race_on = False

            winner = turtle.color()[0]
            if winner == guess:
                print(f"You won! Winner is {winner}")
            else:
                print(f"You lost! Winner is {winner}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


print(winner)

screen.exitonclick()

