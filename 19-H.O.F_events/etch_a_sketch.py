from turtle import Turtle, Screen

tedd = Turtle()
screen = Screen()


def move_forwards():
    tedd.forward(10)


def move_backwards():
    tedd.backward(10)


def rotate_left():
    cuurent_position = tedd.heading()+10
    tedd.setheading(cuurent_position)


def rotate_right():
    cuurent_position = tedd.heading()-10
    tedd.setheading(cuurent_position)


def clear():
    tedd.clear()
    tedd.penup()
    tedd.home()
    tedd.pendown()


# event listeners
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=rotate_left)
screen.onkeypress(key="d", fun=rotate_right)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()
