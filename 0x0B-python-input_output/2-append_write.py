#!/usr/bin/python3
""" This module append text to file """

def append_write(filename="", text=""):
    """ Function appendes text to filename """

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
