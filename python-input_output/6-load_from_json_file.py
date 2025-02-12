#!/usr/bin/python3
"""
Module containing the load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """Loads the object from a json file.

    Args:
    @filename: The file to read from.

    Return:
    The object that was loaded.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
