from turtle import Turtle, Screen

turtle = Turtle()
turtle.color('blue')

color_palette = ["aquamarine2", 'DarkSlateBlue', 'bisque2',
                 'BlueViolet', 'DarkTurquoise', 'DeepPink', "coral4", "DarkOrange1"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):

        turtle.forward(100)
        turtle.right(angle)


for sharp_sides in range(3, 11):
    color = color_palette[sharp_sides - 3]
    turtle.color(color)
    draw_shape(sharp_sides)

screen = Screen()
screen.exitonclick()
