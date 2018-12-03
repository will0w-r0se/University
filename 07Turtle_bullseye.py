from turtle import *


def circle_at(x, y, r, colour):
    penup()
    goto(x, y - r)
    pendown()
    fillcolor(colour)
    begin_fill()
    setheading(0)
    circle(r)
    end_fill()


speed(0)
circle_at(0, 0, 100, "white")
circle_at(0, 0, 80, "black")
circle_at(0, 0, 60, "blue")
circle_at(0, 0, 40, "red")
circle_at(0, 0, 20, "yellow")
hideturtle()

exitonclick()

print()
input("Press return to continue ...")
