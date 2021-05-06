#!/usr/bin/env python3

# Author: Jamie Giannini

# Objectives: Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
# [X] Script must ask the user for a file path and read a user input string into a variable
# [X] Script must use the os.walk() function from the os library
# [X] Script must enclose the os.walk() function within a python function that hands it the user input file path.
# [] Extra: Have the script save the output as a .txt file.
# [] Extra: Have the script open the .txt file with Libre Office Writer.

# Import libraries

import os
import os.path

# Declaration of variables

path = input("Enter a valid file path:")

# Declaration of functions

def file_func(path):
    for root, dirs, files in os.walk(path,topdown=True) :
        ### Print command to print ==files==
        for name in files:
            print(os.path.join(root, name))
        ### Print command to print ==dirs==
        for name in dirs:
            print(os.path.join(root, name))
    return
# Main

file_func(path)

# End