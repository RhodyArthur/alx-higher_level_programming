#!/usr/bin/python3

"""This module contains a function
that returns the object representation
of json"""

import json

def from_json_string(my_str):
    """ Function returns json object """

    return json.loads(my_str)
