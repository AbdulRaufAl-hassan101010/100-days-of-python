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

# event listeners
screen.listen()
# left paddle ctrl
screen.onkeypress(key="Up", fun=left_paddle.up)
screen.onkeypress(key="Down", fun=left_paddle.down)
# right paddle ctrl
screen.onkeypress(key="w", fun=right_paddle.up)
screen.onkeypress(key="s", fun=right_paddle.down)

# create ball
ball = Ball()

is_game_on = True
while is_game_on:
    time.sleep(0.05)

    print(left_paddle.distance(ball) < 10)
    if left_paddle.distance(ball) < 20:
        ball.hit_ball(position="left")
    elif right_paddle.distance(ball) < 20:
        ball.hit_ball(position="right")
    elif ball.ycor() > 280:
        ball.hit_ball(position="top")
    elif ball.ycor() < -280:
        ball.hit_ball(position="top")
    else:
        ball.move_ball()
    screen.update()


# detect ball and paddle collision
# detect ball miss paddle collision
# Keep score


screen.exitonclick()
