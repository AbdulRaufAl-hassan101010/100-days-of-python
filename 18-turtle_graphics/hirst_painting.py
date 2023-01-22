import colorgram
import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
turtle.penup()
turtle.speed('fastest')
turtle.hideturtle()

# set cavas
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)


colors = colorgram.extract('image.jpg', 30)
color_palette = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_palette.append((r, g, b))

number_rows = 10
number_columns = 10
number_of_dots = number_columns * number_rows

for dot_count in range(1, number_of_dots+1):
    turtle.dot(20, random.choice(color_palette))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen = t.Screen()
screen.exitonclick()
