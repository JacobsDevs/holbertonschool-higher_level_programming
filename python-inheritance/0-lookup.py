#!/usr/bin/python3
"""
This is the module containing the lookup function.
"""


def lookup(obj):
    """
    This is the lookup function

    Args:
    @obj: The object to lookup

    Return:
    A list of the objects methods and attributes.
    """
    return dir(obj)
