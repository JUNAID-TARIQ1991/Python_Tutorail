#!/usr/bin/env python3
def mul(x,y):
    print(f"multiplying {x} and {y} ")
    return x*y
def div(x,y):
    print(f"dividing {x} and {y}")
    return x/y

a=float(input("enter any number:"))
b=float(input("enter any number:"))
mult=mul(a,b)
divi=div(a,b)
print(f"{mult},,,,,{divi}")