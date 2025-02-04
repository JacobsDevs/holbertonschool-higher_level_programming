#!/usr/bin/python3
"""
This is the module containing the is_same_class function.
"""


def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
