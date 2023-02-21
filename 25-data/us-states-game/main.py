import turtle
import pandas


screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("./50_states.csv")
guessed_states = []
states = data.state.to_list()


def is_state(state, data):
    new_data = data[data.state == state]
    if len(new_data.index) < 1:
        return False

    return {
        "x": int(new_data.x),
        "y": int(new_data.y),
    }


while len(guessed_states) < 50:
    state = None
    try:
        state = screen.textinput(title=f"Guess a state {len(guessed_states)}/50",
                                 prompt="What is another state name?").title()
    except:
        pass

    # dnt show modal text if user close it
    if state == None or state == 'Exit':
        # get unguessed states and save as a cvs file
        missing_states = [
            missing_state for missing_state in states if missing_state not in guessed_states]

        unguessed_states = pandas.DataFrame(missing_states)
        unguessed_states.to_csv("unguessed_states.csv")
        break

    state_position = is_state(state, data)
    if state_position:
        show_state = turtle.Turtle()
        show_state.penup()
        show_state.hideturtle()
        show_state.goto(x=state_position["x"], y=state_position["y"])
        show_state.write(state, align="center", font=("Arial", 7, "normal"))
        guessed_states.append(state)

    screen.update()
