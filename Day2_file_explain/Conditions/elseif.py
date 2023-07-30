#!/usr/bin/env python3
print("""You enter a dark room with two doors. Do you go through door #1 or door #2?""")
door =input('>')
if door == "1":
    
    print("There's a giant bear here eating a cheese cake.")

    print("What do you do?")

    print("1. Take the cake.")
    print("2. Scream at the bear.")
    bear= input('>')
    if bear=="1":
        print("good go on! ")
    elif bear=="2":
        print("run off dear!")
elif door=="2":
    print("you are safe to go.")

