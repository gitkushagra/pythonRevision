from turtle import Turtle,Screen,colormode
import random

def get_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b
colormode(255)
ringo = Turtle(shape = "turtle")
ringo.color(get_color())
ringo.penup()
limbo = Turtle(shape = "turtle")
limbo.color(get_color())
limbo.penup()
fantoo = Turtle(shape = "turtle")
fantoo.color(get_color())
fantoo.penup()
ribbon = Turtle(shape = "turtle")
ribbon.color(get_color())
ribbon.penup()
furry = Turtle(shape = "turtle")
furry.color(get_color())
furry.penup()

screen = Screen()
screen.setup(width = 500, height = 400)
screen.delay(50)



ringo.goto(x = -238,y=0)
limbo.goto(x = -238,y=30)
fantoo.goto(x = -238,y=60)
ribbon.goto(x = -238,y=-60)
furry.goto(x = -238,y=-30)

all_turtles = [ringo,limbo,fantoo,ribbon,furry]
all_turtle_colors = [ringo.color(),limbo.color(),fantoo.color(),ribbon.color(),furry.color()]


user_bet = screen.textinput(title="Make a bet on colour",prompt="Enter colour name")
try:
    if user_bet not in all_turtle_colors:
        user_turtle = random.choice(all_turtles)
        user_turtle.color(user_bet)
    
except Exception:
    print(Exception)

if user_bet:
    is_race_on = True

while(is_race_on):
    for t in all_turtles:
        if t.xcor() > 230:
            if t.pencolor() == user_bet:
                print(f"You have won! Winning Color: {t.pencolor()}")
            else:
                print(f"You have lost! Winning Color: {t.pencolor()}")
            is_race_on = False
        t.forward(random.randint(0,10))

screen.exitonclick()
