from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.title("Welcome to the NCU Universe")
screen.onkey(key="w", fun=move_forward)
screen.onkey(move_backward, "s")
screen.onkey(key="a", fun=turn_left)
screen.onkey(turn_right, "d")
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
