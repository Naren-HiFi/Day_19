'''
          Day_19 Turtle_Graphics_Event_Listeners_State_And_Multiple_Instances
'''
import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.title("Turtle Race Begins...")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for no_of_turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[no_of_turtle])
    new_turtle.goto(x=-230, y=y_positions[no_of_turtle])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
