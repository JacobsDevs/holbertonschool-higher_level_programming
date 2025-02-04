#!/usr/bin/python3
"""
This is the module containing the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class function:

    Args:
    @obj: The object to check.
    @a_class: The class to check obj against.

    Return:
    True if obj is a_class or a class inherited from a_class.
    False if not.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
