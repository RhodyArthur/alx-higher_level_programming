#!/usr/bin/python3
"""
This 0-add_integer module contains a function 
for integer addition
"""
def add_integer(a, b=98):
    """Validation of addition function"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a + b)
