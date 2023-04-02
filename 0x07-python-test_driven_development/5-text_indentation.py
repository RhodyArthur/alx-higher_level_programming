#!/usr/bin/python3
"""
Text indentation function has a parameter
"""
def text_indentation(text):
    """Function for indentation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in [".", "?", ":"]:
            print("\n\n")
            i += 1
        i += 1
