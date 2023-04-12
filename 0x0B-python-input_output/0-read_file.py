#!/usr/bin/python3
def read_file(filename=""):
    """ Function that reads and print out a text file """
    with open(filename, 'r', encoding="utf-8") as f:
        print("{}".format(f.read(), end="")
