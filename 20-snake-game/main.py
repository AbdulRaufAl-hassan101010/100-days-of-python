import time
from snake import Snake
from game_screen import Game_Screen
from snake_food import Snake_Food
from scoreboard import Scoreboard

game_screen = Game_Screen()
# create snake
snake = Snake()
# create snake food
snake_food = Snake_Food(left_wall=game_screen.left_wall,
                        right_wall=game_screen.right_wall, top_wall=game_screen.top_wall, bottom_wall=game_screen.bottom_wall)
# scores
score = Scoreboard()

# events
game_screen.screen.listen()
game_screen.screen.onkey(key="Up", fun=snake.move_up)
game_screen.screen.onkey(key="Down", fun=snake.move_down)
game_screen.screen.onkey(key="Left", fun=snake.move_left)
game_screen.screen.onkey(key="Right", fun=snake.move_right)


is_game_on = True
while is_game_on:
    time.sleep(0.06)
    game_screen.screen.update()
    snake.move()

    # end game when snake hits the wall
    if snake.head.xcor() > game_screen.right_wall or snake.head.xcor() < game_screen.left_wall or snake.head.ycor() > game_screen.top_wall or snake.head.ycor() < game_screen.bottom_wall:
        score.game_over()
        is_game_on = False

    # dectect collision with food
    if snake.head.distance(snake_food) < 12:
        snake_food.refresh()
        snake.grow_snake()
        score.add_to_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            is_game_on = False
            score.game_over()


game_screen.screen.exitonclick()
