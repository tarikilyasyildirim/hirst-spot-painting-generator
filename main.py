from turtle import Turtle, colormode, done, Screen
import random
import colorgram

tom = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(0, 0, 600, 600)
colormode(255)
tom.speed("fastest")
tom.penup()
tom.hideturtle()
colors = colorgram.extract("picture.jpg", 20)
y = 25

def random_color():
    color = random.choice(colors).rgb
    r, g, b = color.r, color.g, color.b
    while True:
        if r < 220 and g < 220 and b < 220:
            return (r, g, b)
        else:
            return 101, 86, 183

for _ in range(10):
    tom.goto(25, y)
    for _ in range(10):
        tom.dot(20, random_color())
        tom.forward(60)
    y += 60



done()