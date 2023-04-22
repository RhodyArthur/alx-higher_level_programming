#!/usr/bin/python3

""" contains an inherited class Mylist """

class Mylist(list):
    def print_sorted(self):
        """ public instance method that prints sorted list """
        print(sorted(self))
