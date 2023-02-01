from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

# create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Ping  Pong")

screen_divider = Turtle()
screen_divider.color("white")
screen_divider.hideturtle()
screen_divider.penup()
screen_divider.goto(x=0, y=300)
for _ in range(50):
    screen_divider.setheading(270)
    screen_divider.pendown()
    screen_divider.forward(10)
    screen_divider.penup()
    screen_divider.forward(10)


# create and move paddles
left_paddle = Paddle(position=(-350, 0))
right_paddle = Paddle(position=(350, 0))

# create ball
ball = Ball()

# event listeners
screen.listen()
# left paddle ctrl
screen.onkeypress(key="Up", fun=left_paddle.up)
screen.onkeypress(key="Down", fun=left_paddle.down)
# right paddle ctrl
screen.onkeypress(key="w", fun=right_paddle.up)
screen.onkeypress(key="s", fun=right_paddle.down)


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # dectect collision with all
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect ball and paddle collision
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 330) or (ball.distance(left_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
    elif ball.xcor() > 400:
        ball.reset()
    elif ball.xcor() < -400:
        ball.reset()

# detect ball miss paddle collision
# Keep score


screen.exitonclick()
