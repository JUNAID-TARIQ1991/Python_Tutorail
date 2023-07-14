#!/usr/bin/env python3
from sys import argv
from os.path import exists #The os.path module is always the path module suitable for the operating system Python is running on, and therefore usable for local paths. However, you can also import and use the individual modules if you want to manipulate a path that is always in one of the different formats..
script, from_file, to_file =argv
print(f"copying from {from_file} to {to_file}")
in_file =open(from_file) #in_file veriable open the file 
indata =in_file.read() #in_data veriable store the data of file
print(f"the input file is {len(indata)} byte long")
print(f"does the output file exits ? {exists(to_file)}")

out_file = open(to_file, 'w')

out_file.write(indata)
print("alright done!")
out_file.close
in_file.close
