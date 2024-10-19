import random
from turtle import Turtle, Screen
import heroes

timmy = Turtle()

TURNS = ("left","right")
DEGREES = (0,90,180,270)


# timmy.width(10)
timmy.speed(15)
screen = Screen()



# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for i in range(20):
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)
#     timmy.down()



def color_selection():
    return (random.random(), random.random(), random.random())





gap = 5

for i in range(int(360/5)):
    col = color_selection()
    # timmy.setheading(random.choice(DEGREES))
    timmy.color(col)
    # timmy.forward(20)
    timmy.left(gap)
    timmy.circle(100)

screen.exitonclick()