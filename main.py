import random
from turtle import Turtle,Screen

jack = Turtle()
screen = Screen()
jack.speed("fastest")
screen.setup(600,500)
jack.penup()
jack.hideturtle()
x = -225
y = -200
colors = [
    "ForestGreen",
    "SlateBlue",
    "OliveDrab",
    "SteelBlue",
    "RosyBrown",
    "CadetBlue",
    "DarkSeaGreen",
    "Peru",
    "MediumPurple",
    "IndianRed",
    "MediumSeaGreen",
    "Sienna",
    "DarkKhaki",
    "MediumAquamarine",
    "Tan",
    "LightSlateGray",
    "Teal",
    "DarkSalmon",
    "MediumSlateBlue",
    "Burlywood",
    "DarkCyan",
    "Plum",
    "SeaGreen",
    "SandyBrown",
    "PaleVioletRed",
    "MediumTurquoise",
    "Orchid",
    "YellowGreen",
    "LightCoral",
    "CornflowerBlue",
    "Wheat",
    "MediumOrchid",
    "DarkGray",
    "LightSeaGreen",
    "Thistle",
    "Olive",
    "PowderBlue",
    "Coral",
    "MediumSpringGreen",
    "Salmon",
    "DarkTurquoise",
    "Khaki",
    "PaleGreen",
    "Crimson",
    "SkyBlue",
    "Goldenrod",
    "MediumVioletRed",
    "Turquoise",
    "Chocolate",
    "LightSteelBlue"
]

for _ in range(10):
    jack.goto(x, y)
    for _ in range(10):
        jack.dot(30,random.choice(colors))
        jack.forward(50)
    y += 45


screen.exitonclick()
