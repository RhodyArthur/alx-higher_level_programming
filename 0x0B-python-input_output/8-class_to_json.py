#!/usr/bin/python3

""" This module contains a function that returns a dictionary
description with simple data structure. """


def class_to_json(obj):
    """ This function returns the class description """
    return obj.__dict__
