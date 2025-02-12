#!/usr/bin/python3
"""
Module containing the from_json_string function
"""
import json


def from_json_string(my_str):
    """Loads the object from a json string.

    Args:
    @my_str: The string to load.

    Return:
    The string to load into an object.
    """
    return json.loads(my_str)
