# Module: A set of built in functions to perform specific tasks.
''' some commonly used function are print, input, len etc...
'''
'''you can import any module by simply import module name, for example to call a functiob inside math module you 
simpley need to call import math. you can not directly access to function of module'''

# random module




import random
def main():

    print("I am going to print five random number b/w 1 to 100")
    for count in [1, 2, 3, 4, 5, 6]:

        number = random.randint(1, count)

        print("here are the numbers:", number)


main()

'''You will write a while loop that simulates one roll of the dice and then asks the user if
another roll should be performed. As long as the user answers “y” for yes, the loop will
repeat'''


def main():
    again = 'y'
    while again.upper() == 'Y':
        print("rolling the dice")
        print(random.randint(1, 6))
        print(random.randint(1, 6))

        again = input("do you want to roll again hit y >: ")


main()
