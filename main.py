import turtle

turtle.bgcolor("black")
turtle.pensize(1)
turtle.speed(0)

for i in range(6):
    for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()