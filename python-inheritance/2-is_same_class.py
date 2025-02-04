#!/usr/bin/python3
"""
This is the module containing the is_same_class function.
"""


def is_same_class(obj, a_class):
    """
    is_same_class:

    Args:
    @obj: The object to test
    @a_class: The class to test obj against

    Return:
    True if exactly same class.
    False if not.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
