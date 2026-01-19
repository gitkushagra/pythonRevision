from turtle import Turtle,Screen

myturtle = Turtle()
myScreen = Screen()
myturtle.shape("turtle")
myturtle.color("blue")
print(myScreen.canvwidth)
myturtle.forward(100)
myScreen.exitonclick()