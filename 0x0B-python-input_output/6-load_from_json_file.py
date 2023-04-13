#!/usr/bin/python3

""" This modules contains a function that
creates an Object from a JSON file """

import json

def load_from_json_file(filename):
    """ function creates an Object from a JSON file """

    with open(filename) as f:
        line = json.load(f)
        return line
