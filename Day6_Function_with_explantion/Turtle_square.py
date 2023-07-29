import turtle


def tur_polygon(x, y):
    tur = turtle.Turtle()
    tur.penup()
    tur.goto(x, y)
    tur.begin_fill()
    tur.fillcolor("blue")
    tur.pendown()
    for count in range(6):
        tur.forward(100)
        tur.left(60)

    tur.end_fill()


def main():
    tur_polygon(0, 0)

    tur_polygon(-100, -200)
    turtle.done()


main()
