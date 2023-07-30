#!/usr/bin/env python3
people=int(input("how many people?"))
cats=int(input("how many cats?"))
dogs=int(input("how many dogs?"))
if people < cats :
    print("too many cats!")
if cats < people:
    print("we are saved.")
if dogs > people:
    print ("too many dogs.")