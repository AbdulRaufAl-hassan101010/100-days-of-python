from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Ping  Pong")


# create and move paddles
left_paddle = Paddle(position=(-350, 0))
right_paddle = Paddle(position=(350, 0))

# create ball
ball = Ball()
scoreboard = Scoreboard()

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
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # dectect collision with all
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect ball and paddle collision
    elif (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    elif ball.xcor() > 390:
        ball.reset()
        scoreboard.increase_left_score()
    elif ball.xcor() < -390:
        ball.reset()
        scoreboard.increase_right_score()


# detect ball miss paddle collision
# Keep score


screen.exitonclick()
