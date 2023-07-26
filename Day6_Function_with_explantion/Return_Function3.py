def main():
    # Take three numbers from the user and store them as width, height, and length
    # bydefault python indent a line by four spaces in a block of code.
    print("Enter the parameters of the rectangle")
    width, height, length = get_input()  # unpacking
    print("You have entered the following parameters")
    Display_params(width, height, length)


def get_input():

    width = int(input("Enter the width > "))
    height = int(input("Enter the height > "))
    length = int(input("Enter the length > "))
    return width, height, length


def Display_params(width, height, length):
    print("Width:", width)
    print("Height:", height)
    print("Length:", length)


main()

"""Explanatio
The main() function is the entry point of the program. 
It first prompts the user to enter the parameters of a rectangle (width, height, and length).

The get_input() function is defined to take three numbers as input from the user, 
representing the width, height, and length of the rectangle. The input is collected using the input() function, 
and the user's input is converted to integers using int().

The get_input() function returns the three input values (width, height, and length) as a tuple.

Back in the main() function, the returned values (width, height, 
and length) are unpacked from the tuple and assigned to the respective variables.

After getting the user's input, the program proceeds to call the Display_params() function, 
passing the width, height, and length as arguments.

The Display_params() function takes the three arguments (width, height, and length) and simply prints them out along with their labels ("Width:", "Height:", "Length:").

Finally, the main() function is called to start the execution of the program."""
