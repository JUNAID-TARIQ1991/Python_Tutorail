def main():
    # Dispalay the message
    startup_message()
    # prompt the user to see first step
    input("Hit enter to see the first step >")
    step_one()
    input("Hit enter to see second step >")
    step_two()
    input("Hit enter to see third step >")

    step_three()
    input("Hit enter to see fourth step >")
    step_four()


def startup_message():
    print()

    print("This program tells you\nhow to disassemble the dryer")
    print()


def step_one():
    print("Step 1: Unplug the dryer\nand move it away from wall")
    print()


def step_two():
    print("Step 2: Remove the six screew \nfrom the back of the dryer")
    print()


def step_three():
    print("Step 3: Remove the back pannel from the dryer")
    print()


def step_four():
    print("Remove the head of the dryer")
    print()


main()
