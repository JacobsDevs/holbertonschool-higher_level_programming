#!/usr/bin/python3
"""
This is the module that contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    inherits_from:

    Args:
    @obj: The object to check.
    @a_class: The class the check obj against.

    Return:
    True if a subclass.
    False if not.
    """

    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
