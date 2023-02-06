from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 280:
            x = self.xcor()
            y = self.ycor() + 20
            self.goto(x, y)

    def down(self):
        if self.ycor() > -280:
            x = self.xcor()
            y = self.ycor() - 20
            self.goto(x, y)
