#!/usr/bin/python3
def write_file(filename="", text=""):
    """ Function that writes to a text file
    and return number of characters """

    with open(filename, 'w') as f:
        return f.write(text)
