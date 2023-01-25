from turtle import Turtle, Screen
import random

# setup screen
screen = Screen()
screen.setup(width=500, height=400)

# place bet
bet = screen.textinput(title="Place Your Bet",
                       prompt="Who will win the race, enter the color? ").lower()
print(bet)

colors = ["red", "yellow", "green", "pink", "blue", "orange"]
position_y = [-70, -40, -10, 20, 50, 80]
racers = []
for racer_index in range(6):
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(colors[racer_index])
    racer.goto(x=-230, y=position_y[racer_index])
    racers.append(racer)


race_ended = False
winner = 0
while race_ended != True:
    for racer in racers:
        racer.forward(random.randint(0, 10))

        if racer.xcor() > 230 and winner == 0:
            race_ended = True
            winner = racer.pencolor()

if winner == bet:
    print(f"You win, {winner} pink won the race.")
else:
    print(f"You loss, {winner} won the race.")
# screen.exitonclick()
