from turtle import Turtle, colormode, Screen
import random

turtle = Turtle()
turtle.pensize(15)
turtle.speed("fastest")
colormode(255)
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(200):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
