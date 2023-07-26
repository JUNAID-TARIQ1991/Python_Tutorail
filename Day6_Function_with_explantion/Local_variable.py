def main():
    get_name()
    # Here the name cannot be access! because name is local veriable for get_name function.anget_name():
    print("name: ", name)


def get_name():

    name = input("Enter your name >")


main()

# similarly
'''def bad_function():
print('The value is', val) #local veriable only access after its creation
val = 99'''
# That is why we can use veriable with same name in more then one function
# example
# This program demonstrates two functions that
# have local variables with the same name.


def main():
    # Call the texas function.
    texas()
# Call the california function.
    california()
# Definition of the texas function. It creates
# a local variable named birds.


def texas():
    birds = 5000
    print('texas has', birds, 'birds.')
# Definition of the california function. It also
# creates a local variable named birds.


def california():
    birds = 8000
    print('california has', birds, 'birds.')


# Call the main function.
main()
