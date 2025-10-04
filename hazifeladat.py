# házi feladat

import turtle

def sokszog():
    turtle.penup()
    turtle.goto(-100,100)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.pensize(6)

    for _ in range(8):
        turtle.forward(100)
        turtle.right(45)


def rajzol():
    turtle.hideturtle()
    turtle.clear()
    sokszog()


ablak=turtle.Screen()

#turtle.done()
turtle.listen()
turtle.onkey(rajzol, 'a')
turtle.onkey(turtle.bye, 'b')
turtle.mainloop()