from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color("white")
        self.move_ball()
        self.setheading(random.randint(150, 220))

    def move_ball(self):
        self.forward(10)

    def hit_ball(self, position):
        if position == "left":
            top = random.randint(0, 90)
            down = random.randint(270, 360)
        elif position == "right":
            top = random.randint(45, 90)
            down = random.randint(275, 325)
        elif position == "top":
            top = random.randint(275, 325)
            down = random.randint(275, 325)
        elif position == "bottom":
            top = random.randint(45, 90)
            down = random.randint(45, 90)

        self.setheading(random.choice([top, down]))
        self.move_ball()
