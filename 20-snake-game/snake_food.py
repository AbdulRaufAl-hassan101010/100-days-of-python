import random
from turtle import Turtle


class Snake_Food(Turtle):
    def __init__(self, left_wall, right_wall, bottom_wall, top_wall):
        super().__init__()

        self.left_wall = left_wall
        self.right_wall = right_wall
        self.bottom_wall = bottom_wall
        self.top_wall = top_wall

        # create food
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        self.refresh()

    def refresh(self):
        """Change the food position (x, y)"""
        position_x = random.randint(self.left_wall, self.right_wall)
        position_y = random.randint(self.bottom_wall, self.top_wall)

        # set position
        self.goto(x=position_x, y=position_y)
