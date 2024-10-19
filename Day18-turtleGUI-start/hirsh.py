import turtle

import colorgram
import random
from turtle import Turtle, Screen
import heroes
turtle.colormode(255)
timmy = Turtle()

TURNS = ("left","right")
DEGREES = (0,90,180,270)
timmy.up()
timmy.hideturtle()
timmy.setpos(x=-100, y=-100)
# timmy.width(10)
timmy.speed("fastest")

screen = Screen()
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    rgb_colors.append((float(color.rgb.r), float(color.rgb.g), float(color.rgb.b)))


color_list = [(250, 248, 241), (251, 244, 248), (243, 250, 247), (241, 246, 251), (234, 224, 83), (189, 10, 69), (196, 76, 20), (111, 180, 212), (215, 163, 101), (193, 164, 19), (32, 104, 164), (226, 58, 129), (209, 137, 177), (14, 24, 66), (21, 31, 159), (190, 39, 118), (39, 185, 114), (229, 167, 198), (18, 181, 209), (231, 222, 10), (128, 187, 159), (10, 49, 29), (45, 129, 78), (59, 12, 28), (69, 22, 8), (174, 20, 11), (134, 216, 231), (232, 67, 36), (152, 213, 196), (114, 91, 204)]


for j in range(10):
    for i in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.up()
        timmy.fd(50)
    timmy.back(500)
    timmy.left(90)
    timmy.fd(50)
    timmy.right(90)


screen.exitonclick()