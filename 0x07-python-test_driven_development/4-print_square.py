#!/usr/bin/python3
"""
Print square module
"""
def print_square(size):
    """Function prints a square using #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    print((size * '#' + '\n') * size,end='')
