#!/usr/bin/env python3
from sys import argv
script, file_name =argv
txt = open(file_name)
print(txt.read())
print("Type the filename again:")
file_again =input(">")
txt_again=open(file_again)
print(txt_again.read())

#A few fancy things are going on in thisfile, so let’s break it down real quickly: • Lines 1–3 use argv to
#get a filename. Next we have line 5, where we use a new command,
#open. Right now, run pydoc open and read the instructions. Notice
#how, like your own scripts and input, it takes a parameter and
#returns a value you can set to your own variable. You just opened a
#file.
