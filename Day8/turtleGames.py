from turtle import Turtle,Screen,colormode
import random


def get_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

def draw_spirograph(turtleObj,gap_size,radius):
    for _ in range(360 // gap_size):
        turtleObj.color(get_colour())
        turtleObj.circle(radius)
        turtleObj.setheading(turtleObj.heading() + gap_size)
     

def randomWalk(turtleObj,steps):
    turtleObj.forward(steps)
    turtleObj.setheading(random.choice([0, 90, 180, 270]))
    

def draw_shape(turtleObj,sides,steps):
    myTurtle.color(get_colour())
    angle = 360 / sides
    for _ in range(sides):
        turtleObj.forward(steps)
        turtleObj.right(angle)

def draw_dash_line():
    for _ in range(10):
        myTurtle.forward(10)
        posX = myTurtle.position()[0] + 10
        myTurtle.teleport(x=posX,y=None,fill_gap=False)

   
myTurtle = Turtle()
colormode(255)
myScreen = Screen()
# myScreen.delay(1)
myTurtle.speed("fastest")

draw_spirograph(myTurtle,5,100)
# for sides in range(3,15):
#     draw_shape(myTurtle,sides,100)

# myTurtle.pensize(10)


# for _ in range(300):
#     myTurtle.color(get_colour())
#     randomWalk(myTurtle,30)

myScreen.exitonclick()
