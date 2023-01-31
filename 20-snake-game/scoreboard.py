from turtle import Turtle
from game_screen import Game_Screen


class Scoreboard(Turtle, Game_Screen):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.display_score()

    def display_score(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 225)
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 16, "normal"))

    def add_to_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over!!", align="center",
                   font=("Arial", 16, "normal"))
