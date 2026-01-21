###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram



# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r =color.rgb[0]
#     g =color.rgb[1]
#     b =color.rgb[2]
#     rgb_colors.append((r,g,b))

# print(rgb_colors)

from turtle import Turtle,Screen,colormode
import random
colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def get_color():
    return random.choice(colors)

def get_pos(obj_turtle):
    return obj_turtle.position()[0],obj_turtle.position()[1]

my_screen = Screen()
cute_turtle = Turtle()
cute_turtle.pensize(10)
colormode(255)
cute_turtle.hideturtle()

current_pos = get_pos(cute_turtle)
x_axis_initial = current_pos[0]
y_axis_initial = current_pos[1]
y_incremetal = 50

for y in range(10):
    for x in range(10):
        current_pos = get_pos(cute_turtle)
        cute_turtle.pencolor(get_color())
        cute_turtle.dot(20)
        cute_turtle.teleport(x=current_pos[0]+50,y= None,fill_gap=False)
    cute_turtle.teleport(x= x_axis_initial, y = x_axis_initial+y_incremetal,fill_gap=False)
    y_incremetal += 50

my_screen.exitonclick()




