import Circle
import rectangle

circle_area_choice = 1
circle_circum_choice = 2
rect_area_choice = 3
rect_peri_choice = 4
Quit_choice = 5


def main():
    choice = 0
    while choice != Quit_choice:
        display_menu()
        choice = int(input("Enter your choice: >"))
        print()
        if choice == circle_area_choice:
            radius = int(input("Enter the radius of circle: "))
            print("The area of circle will be:", Circle.area(radius))
        elif choice == circle_circum_choice:
            radius = int(input("Enter the radius of circle: "))
            pritn("The Circumference of circle is: ",
                  Circle.cicumference(radius))
        elif choice == rect_area_choice:
            width = float(input("Enter the width of a rectangle"))
            length = float(input("Enter the length of rectange"))
            print("The area of rectangle is: ", rectangle.area(length, width))
        elif choice == rect_peri_choice:
            width = float(input("Enter the width of a rectangle"))
            length = float(input("Enter the length of rectange"))
            print("The peri of rectangle is: ",
                  rectangle.perimeter(length, width))
        elif choice == Quit_choice:
            print("Exiting the program .....")
            exit()
        else:
            print("Invalid choice")


def display_menu():
    print(' MENU')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')


main()
