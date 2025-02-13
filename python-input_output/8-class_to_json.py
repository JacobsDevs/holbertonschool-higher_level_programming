#!/usr/bin/python3
"""
Module containing the class_to_json function
"""


def class_to_json(obj: object):
    """Returns the JSON serialization of an object in dictionary form.

    Args:
    @obj: The object to serialize

    Return:
    JSON representation of the class that was serialized.
    """
    return obj.__dict__
