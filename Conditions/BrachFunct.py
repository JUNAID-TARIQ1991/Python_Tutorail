"""This code is a Python script that defines three functions (gold_room(), bear_room(),
and cthulhu_room()) and uses them to create a simple text-based game.

The gold_room() function prompts the user to enter a number and then checks whether the input is 0 or 1.
If it is, the function sets a variable howmuch to the integer value of the input. If not, 
the function calls the dead() function with an error message. The function then checks if howmuch is less 
than 50,
and prints a message accordingly, or calls the dead() function with an error message.

The bear_room() function prompts the user to enter a command and responds accordingly. 
If the user enters "take honey", the function calls the dead() function with an error message.
If the user enters "taunt bear" and the bear has not yet been moved, 
the function prints a message indicating that the bear has moved, and sets a variable bear_moved to True.
If the user enters "taunt bear" and the bear has already been moved, the function calls the dead() function with an error message. 
If the user enters "open door" and the bear has been moved, the function calls the gold_room() function. If the user enters any other command, 
the function prints a message indicating that it doesn't understand the command.

The cthulhu_room() function simply prints a message about the "great evil Cthulhu".

The rest of the code defines the dead() function, which prints an error message and exits the script,
and calls the start() function, which prompts the user to choose between two doors. If the user enters 
"left", the bear_room() function is called. If the user enters "right", the cthulhu_room() function is called. If the user enters anything else, 
the dead() function is called with an error message, and the start() function is called again.

Note that the start() function is defined after the call to cthulhu_room(), 
so it will never actually be called. Also, the raw_input() function used in this code is not valid in 
Python 3.x, it should be replaced with input().
"""
#!/usr/bin/env python
from sys import exit

# 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 API


def gold_room():
    print("This room is full of gold, how much will you take?")
    
    next = input(">")
    if "0" in next or "1" in next:
        howmuch = int(next)
    else:
        dead("Man,Learn to type a number")
    if howmuch < 50:
        print("You are not greedy U Win")
        exit(0)
    else:
         dead("you greedy bastard")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    while True:
        next = input("> ")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    next = input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    next = input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
start()
