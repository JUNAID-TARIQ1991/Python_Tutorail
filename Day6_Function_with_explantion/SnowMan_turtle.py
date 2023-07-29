import turtle


def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_snowman():
    # Set up the turtle
    turtle.speed(0)
    turtle.bgcolor("sky blue")

    # Draw the snowman body
    draw_circle("white", 30, 0, -40)
    draw_circle("white", 40, 0, -100)
    draw_circle("white", 60, 0, -200)

    # Draw the snowman's eyes
    draw_circle("black", 2, -15, -10)
    draw_circle("black", 2, 15, -10)

    # Draw the snowman's nose
    draw_circle("orange", 2, 0, -15)

    # Draw the snowman's buttons
    draw_circle("black", 2, 0, -35)
    draw_circle("black", 2, 0, -45)
    draw_circle("black", 2, 0, -55)

    # Draw the snowman's arms
    turtle.penup()
    turtle.goto(-20, -28)
    turtle.pendown()
    turtle.goto(-40, -20)

    turtle.penup()
    turtle.goto(20, -28)
    turtle.pendown()
    turtle.goto(40, -20)

    # Draw the snowman's hat
    turtle.penup()
    turtle.goto(-35, 8)
    turtle.pendown()
    turtle.goto(35, 8)
    turtle.goto(30, 8)
    turtle.goto(30, 18)
    turtle.goto(-30, 18)
    turtle.goto(-30, 8)
    turtle.goto(-35, 8)

    # Hide the turtle and display the drawing
    turtle.hideturtle()
    turtle.done()


# Call the function to draw the snowman
draw_snowman()
