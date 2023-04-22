#!/usr/bin/python3
"""contains inherits_from function"""


def inherits_from(obj, a_class):
    """
    returns True if the object isinstance of a class that inherited
    """
    return (issubclass(type(obj)), a_class) and type(obj) != a_class)
