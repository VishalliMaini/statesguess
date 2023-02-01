from turtle import Turtle
import pandas as pd
from turtle import Screen
screen=Screen()
screen.title("Us state game")
img="blank_states_img.gif"
screen.addshape(img)
t=Turtle()
t.shape(img)

df=pd.read_csv("50_states.csv")
all_states=df.state.to_list()
guessed_state=[]
while len(guessed_state)<50:
    ans = screen.textinput(title=f"{len(guessed_state)}/50 guessed", prompt="What is another state name?").title()
    if ans=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        print(missing_states)
        break
    if ans in all_states:
        guessed_state.append(ans)
        x=int(df[df.state==ans].x)
        y=int(df[df.state==ans].y)
        state=Turtle()
        state.penup()
        state.hideturtle()

        state.goto(x, y)

        state.hideturtle()

        state.write(f"{ans}")


