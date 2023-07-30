#!/usr/bin/env python3
i=0
number=[]
while i < 6:
    print(f"now i is {i}" )
    number.append(i)
    i=i+1

print("numbers now:", number)
for num in number:
    print(f"{num}")