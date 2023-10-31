from turtle import Turtle, Screen

import pandas
import pandas as pd

# set up the screen parameters (background etc)
screen = Screen()
screen.title("U.S. States Game")
screen.bgcolor('cadet blue')
screen.bgpic("blank_states_img.gif")

turtle = Turtle()
turtle.penup()
turtle.hideturtle()


df = pd.read_csv("50_states.csv")

correct_answers = []

while len(correct_answers) < 50:
    # ask the user to guess a state
    answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in df.state:
            if state not in correct_answers:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    # check if there is such state in U.S.A
    for state in df.state:
        if state == answer_state:
            state_data = df[df.state == answer_state]  # get the corresponding row
            turtle.goto(int(state_data.x), int(state_data.y))  # write the U.S. state to the correct location
            turtle.write(answer_state)
            correct_answers.append(answer_state)

# when the game ends
turtle.goto(-90, 270)
turtle.write('GAME OVER', font=('Arial', 19, 'bold'))
