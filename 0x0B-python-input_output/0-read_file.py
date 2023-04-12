#!/usr/bin/python3
""" This module reads and print out a file """

def read_file(filename=""):
    """ Function takes in filename as argument
    then output content of file to screen
    """
    
    with open(filename, 'r', encoding="utf-8") as f:
        print("{}".format(f.read(), end="")
