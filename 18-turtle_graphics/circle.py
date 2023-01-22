import turtle as t
import random

turtle = t.Turtle()
turtle.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_sparograph(size_of_gap):
    turns = int(360 / size_of_gap)
    for _ in range(turns):
        turtle.color(random_color())
        heading = turtle.heading()
        turtle.setheading(heading + size_of_gap)
        turtle.circle(100)


draw_sparograph(5)


screen = t.Screen()
screen.exitonclick()
