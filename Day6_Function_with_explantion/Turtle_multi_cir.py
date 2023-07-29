import turtle

colors = ['red', 'blue', 'green', 'amber', 'yellow', 'violet']


def mult_circ(x, y, radius):
    tur = turtle.Turtle()
    turtle.bgcolor("white")
    tur.penup()
    tur.goto(x, y)

    for count in range(6):
        tur.fillcolor(colors[count])
        tur.begin_fill()
        tur.pencolor(colors[count])
        tur.circle(radius*count)
        tur.end_fill()


def main():
    mult_circ(0, 0, 100)
    turtle.done()


main()
