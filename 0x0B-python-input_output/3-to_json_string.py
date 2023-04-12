#!/usr/bin/python3
""" This module contains function which
returns the json representation of
string """

import json

def to_json_string(my_obj):
    """ Function returns json string """
    return json.dumps(my_obj)
