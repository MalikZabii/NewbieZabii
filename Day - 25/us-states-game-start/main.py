import turtle
import pandas
import time

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Try to load the image and handle errors
image = "blank_states_img.gif"
try:
    screen.addshape(image)
    turtle.shape(image)
except Exception as e:
    print(f"Error loading image: {e}")
    time.sleep(5)
    exit()

# Try to read the CSV file and handle errors
try:
    data = pandas.read_csv("50_states.csv")
except FileNotFoundError:
    print("Error: 50_states.csv file not found.")
    time.sleep(5)
    exit()

all_states = data.state.to_list()
guessed_states = []

# Game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # Save the missing states to a new CSV file
        missing_states = [
            state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# Keeps the window open until manually closed
turtle.mainloop()
