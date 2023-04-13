#!/usr/bin/python3

""" This module contains a class: student """


class Student:
    """ this is a student class """

    def __init__(self, first_name, last_name, age):
        """ This method instantiates a student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method that return a dictionary
        Depending the attributes
        """
        if type(attrs) is not list:
            return self.__dict__
        dict = {}

        for i in attrs:
            validate = getattr(self, i, None)
            if validate is not None:
                dict[i] = validate
        return dict
      
    def reload_from_json(self, json):
        """ This method replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
