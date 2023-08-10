import turtle


def main():
    class Draw_shapes:
        def __init__(self, x, y, width, color):
            self.x = x
            self.y = y
            self.width = width
            self.color = color

        def square(self):
            turtle.penup()
            turtle.goto(self.x, self.y)
            turtle.fillcolor(self.color)
            turtle.pendown()
            turtle.begin_fill()
            for count in range(4):
                turtle.forward(self.width)
                turtle.left(90)
            turtle.end_fill()

        def polygon(self):
            tur = turtle.Turtle()
            tur.penup()
            tur.goto(self.x, self.y)
            tur.fillcolor(self.color)
            tur.begin_fill()
            tur.pendown()
            for sides in range(6):
                tur.forward(self.width)
                tur.right(60)
            tur.end_fill
    shape1 = Draw_shapes(-100, -100, 200, 'red')
    shape1.square()
    shape1.polygon()


main()
turtle.done()
tur.done()
