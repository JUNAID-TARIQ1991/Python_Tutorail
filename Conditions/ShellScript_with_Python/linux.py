#!/usr/bin/env python3
import os
# how to print the directory you working in. 
CWD=os.getcwd()
print(f"{CWD}")


#how to change current working directory
os.chdir('/home/junaid/')
print("Current working directory: {0}".format(os.getcwd()))



import os

path = '/home/junaid/p/'

try:
    os.chdir(path)
    print("Current working directory: {0}".format(os.getcwd()))
except FileNotFoundError:
    print("Directory: {0} does not exist".format(path))
except NotADirectoryError:
    print("{0} is not a directory".format(path))
except PermissionError:
    print("You do not have permissions to change to {0}".format(path))