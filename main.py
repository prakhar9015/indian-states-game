import turtle as t
import pandas

screen = t.Screen()
screen.setup(870, 800)
screen.title("India States Game")
image = "india_bharat.gif"
screen.addshape(image)
t.shape(image)

screen.tracer(0)


def neighbour_countries():

    font_name = "Courier"

    tim = t.Turtle()
    tim.speed(0)
    tim.hideturtle()
    tim.penup()
    tim.pencolor("green")

    tim.goto(94, 292)
    tim.write("China", font=(font_name, 14, "normal"))
    ###
    tim.goto(-30, 169)
    tim.write("Nepal", font=(font_name, 14, "normal"))
    ###
    tim.goto(159, 136)
    tim.write("Bhutan", font=(font_name, 13, "normal"))
    ###
    tim.goto(-350, 221)
    tim.write("Pakistan", font=(font_name, 13, "normal"))
    ###
    tim.goto(139, 63)
    tim.write("Bangladesh", font=(font_name, 12, "normal"))
    ###
    tim.goto(265, -27)
    tim.write("Myanmar", font=(font_name, 15, "normal"))
    ###


screen.update()

# ------ Pandas data analysis ---------

data = pandas.read_csv("Indian_states.csv")
states_list = data.state.to_list()


# current_state = data[data.state == "Bihar"]  # dataframe
# print(current_state.capital)  # series
# print(current_state.capital.iloc[0])

# -------------------------------------------------------------------------------------


def display_answers(state_name, state_color, capital_color):
    """ Takes user_answer and checks for the x and y-axis using pandas and construct a turtle
     object that takes a "color" of choice and writes to that position """
    current_state = data[data.state == state_name]  # data checking

    x_axis = int(current_state.x.iloc[0])  # int(ser.iloc[0]) else get FutureWarning
    y_axis = int(current_state.y.iloc[0])

    # also find the capital name
    capital = current_state.capital.iloc[0]

    # change coordinates into tuples
    axis_tuple = (x_axis, y_axis)

    capital_tuple = (x_axis, y_axis - 13)

    tim = t.Turtle()
    tim.hideturtle()
    tim.speed(1)
    tim.penup()
    tim.goto(axis_tuple)
    tim.pencolor(state_color)
    tim.write(state_name, font=('Courier', 9, 'normal'))  # font=('Courier', 8, 'normal')

    timmy = t.Turtle()
    timmy.hideturtle()
    timmy.speed(1)
    timmy.penup()
    timmy.goto(capital_tuple)
    timmy.pencolor(capital_color)
    timmy.write(capital)  #


def congratulate_winner():
    """ when user has filled all the states correctly, then constructs a turtle and writes to the top of the game"""
    tim = t.Turtle()
    tim.hideturtle()
    tim.penup()
    tim.goto(-37.0, 257.0)
    tim.pencolor("purple2")
    tim.write("Congratulations ! You answered all correctly", align='center', font=('Papyrus', 18, 'bold'))


# --------- Game starts here ---------

game_on = True
user_correct_answers = []

while game_on:
    screen.update()
    neighbour_countries()

    user_answer = screen.textinput(title=f"{len(user_correct_answers)}/{len(states_list)} states correct",
                                   prompt="Enter state name: ").title()

    if user_answer in states_list and user_answer not in user_correct_answers:
        display_answers(user_answer, "blue", "magenta")  # call that function

        # put all the user_answer in a list
        user_correct_answers.append(user_answer)

        if len(user_correct_answers) == len(states_list):
            game_on = False
            congratulate_winner()

    elif user_answer == "Exit":  # because all inputs is converted in Title case
        game_on = False
        remaining_states = []

        for i in states_list:
            if i not in user_correct_answers:
                remaining_states.append(i)
                display_answers(i, "red", "DeepPink")

                # create a file that shows the left out states
                list_dataframe = pandas.DataFrame(remaining_states)
                list_dataframe.to_csv("remaining_states.txt")

t.mainloop()
