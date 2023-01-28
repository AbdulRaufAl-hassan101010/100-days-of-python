from turtle import Screen


class Game_Screen:
    def __init__(self, width=600, height=500):
        self.screen = Screen()
        self.screen_width = width
        self.screen_height = height
        self.config_screen()
        self.left_wall = (self.screen_width * - 1) / 2 + 20
        self.right_wall = self.screen_width / 2 - 20
        self.top_wall = self.screen_height / 2 - 20
        self.bottom_wall = (self.screen_height * -1) / 2 + 20

    def config_screen(self):
        self.screen.setup(width=self.screen_width, height=self.screen_height)
        self.screen.bgcolor("black")
        self.screen.title("snake game")
        self.screen.tracer(0)
