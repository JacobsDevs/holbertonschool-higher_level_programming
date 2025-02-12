#!/usr/bin/python3
"""
Module containing the save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """Saves the object as a json string to txt file.

    Args:
    @my_obj: The object to save.
    @filename: The file to save it to.

    Return:
    None
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
