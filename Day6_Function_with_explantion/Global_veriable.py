# create a global veriable #Although you should try to avoid the use of global variables
number = 0


def show_number():
    print("The number you entered is", number)


def main():
    global number
    number = int(input("Enter any number: "))
    show_number()


main()

'''The assignment statement in line 2 creates a global variable named number. Notice inside
the main function, line 5 uses the global key word to declare the number variable. This
statement tells the interpreter that the main function intends to assign a value to the global
number variable.'''
