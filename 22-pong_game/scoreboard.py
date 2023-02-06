from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(x=-100, y=195)
        self.write(self.left_score, align="center",
                   font=('Arial', 50, 'normal'))
        self.goto(x=100, y=195)
        self.write(self.right_score, align="center",
                   font=('Arial', 50, 'normal'))

    def increase_left_score(self):
        self.clear()
        self.left_score += 1
        self.update_score()

    def increase_right_score(self):
        self.clear()
        self.right_score += 1
        self.update_score()
