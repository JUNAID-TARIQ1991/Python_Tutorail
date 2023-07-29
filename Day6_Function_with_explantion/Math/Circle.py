import math
import matplotlib as plt


def area(radius):
    return math.pi * radius**2  # in math module pi is an builtin function


def cicumference(radius):
    return 2 * math.pi * radius


def main():
    print("Enter the radius of circle in meters:")
    radius = int(input(">"))
    print("The area of the circle is in m2: ", area(radius))


main()
