#!/usr/bin/env python3
from sys import argv
script, file1=argv


def print_all(f):
    print(f.read())
#def rewind(f):
    #f.seek(0)
def printaline(line_count,f):
    print(line_count,f.readline())
currentfile=open(file1)

print("let's print the whole file")
print_all(currentfile)
#print("now lets rewind")
#rewind(currentfile)
print("lets print first lines")
printaline(1,currentfile)

