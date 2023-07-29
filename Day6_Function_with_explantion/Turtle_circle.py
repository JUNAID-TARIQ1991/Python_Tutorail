import turtle


def tur_circle(x, y, radius, color):
    tur = turtle.Turtle()
    tur.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    tur.fillcolor('red')
    tur.begin_fill()
    tur.pendown()
    tur.circle(radius)
    tur.end_fill()


def tur_triangle(x, y):
    tur = turtle.Turtle()
    turtle.penup()
    turtle.goto(x, y)
    tur.fillcolor('red')
    tur.begin_fill()
    tur.pendown()
    for count in range(2):
        tur.forward(100)
        tur.right(90)
        if count == 2:
            tur.left(60)
    tur.end_fill()


def main():
    turtle.hideturtle()
    tur_circle(0, 0, 100, 'red')
    tur_triangle(-500, -500)
    turtle.done()


main()
