#!/usr/bin/python3
"""This is the 3-say_my_name module which contains the say_my_name function:
Args:
    first_name: The first name to be printed.
    last_name: The last name to be printed.
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is `first_name` `last_name`
    """
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
    except ValueError:
        if not isinstance(first_name, str):
            raise TypeError('first_name must be a string')
        if not isinstance(last_name, str):
            raise TypeError('last_name must be a string')
