from turtle import Screen
import time
from snake import Snake

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)


segments = []
score = 0
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake()

# events
screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)


is_game_on = True
while is_game_on:
    # end game when snake hits the wall
    left_wall = (SCREEN_WIDTH * - 1) / 2
    right_wall = SCREEN_WIDTH / 2
    top_wall = SCREEN_HEIGHT / 2
    bottom_wall = (SCREEN_HEIGHT * -1) / 2
    if snake.head.xcor() > right_wall or snake.head.xcor() < left_wall or snake.head.ycor() > top_wall or snake.head.ycor() < bottom_wall:
        is_game_on = False

    time.sleep(0.1)
    screen.update()
    snake.move()


screen.exitonclick()
