#!/usr/bin/env python3
#print ("how old are you?", end='') # end='' take input at the same lin#e
#age= input()
#print("how tall you are?", end='')
#height= input()
#print ("how much weight you have?", end='')
#weight=input()
#print("so,you are %r old %r tall and have %r weight" %(age, height, weight))#

name = input("What is your name dear?")
age =input("how old are you? ")
height =input("how tall you are? ")
weight =input("how much weight do you have? ")
print(f"so, you are {age} year old, {height} tall and weigh {weight}") # with you can print the value directly in {}
print("Good bye %s"%name)