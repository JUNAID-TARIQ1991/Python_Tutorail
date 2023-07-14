#!/usr/bin/env python3 
from sys import argv
script, filename = argv
print("first clean the file %r"%filename)
print("opening file %s"%filename)
target=open(filename,'w')
target.truncate()
target.write("Hi python \n")
target.close
