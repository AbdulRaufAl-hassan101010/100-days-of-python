from turtle import Turtle
from game_screen import Game_Screen


class Scoreboard(Turtle, Game_Screen):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.get_high_score()
        self.display_score()

    def save_high_score(self):
        with open("highscore.txt", mode="w") as file:
            file.write("0")

    def get_high_score(self):
        try:
            with open("highscore.txt") as file:
                self.highscore = int(file.read())
        except:
            self.save_high_score()

    def display_score(self):
        self.clear()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 225)
        self.write(f"Highscore:{self.highscore} Score:{self.score}", align="center",
                   font=("Arial", 16, "normal"))

    def add_to_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over!!", align="center",
                   font=("Arial", 16, "normal"))

        if self.score > self.highscore:
            self.save_high_score()
            self.display_score()
