from turtle import Turtle, Screen

limbo = Turtle()
screen = Screen()


def move_forwards():
    limbo.forward(10)

def move_backward():
    limbo.backward(10)

def rotate_set_clockwise():
    limbo.right(10)

def rotate_set_counter_clockwise():
    limbo.left(10)
   
def clear_drawing():
    limbo.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key = "s", fun =move_backward)
screen.onkey(key = "a",fun = rotate_set_counter_clockwise)
screen.onkey(key = "d", fun = rotate_set_clockwise)
screen.onkey(key = "c", fun = clear_drawing)

screen.exitonclick()

