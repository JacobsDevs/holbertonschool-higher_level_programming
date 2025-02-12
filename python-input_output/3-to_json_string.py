#!/usr/bin/python3
"""
Module containing the to_json_string function
"""
import json


def to_json_string(my_obj):
    """Dumps the object to a json string.

    Args:
    @my_obj: The object to dump.

    Return:
    The json dumped object as a string
    """
    return json.dumps(my_obj)
