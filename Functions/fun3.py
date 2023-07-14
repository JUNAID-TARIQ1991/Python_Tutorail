#!/usr/bin/env python3
def add(a,b):
    print(f"adding {a} and {b}")
    return a+b
def mul(a,b):
    print(f"multiplying {a} and {b}")
    return a*b
def div(a,b):
    print(f"dividing {a} and {b}")
    return a/b
x=add(25,56)
y=mul(34,78)
z=div(12,69)
print(f"add: {x} mul: {y} div: {z}")
what=add(x,mul(div(34,12),3)) #######what is this?
print(f"{what}")