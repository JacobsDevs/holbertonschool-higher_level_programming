#!/usr/bin/python3
"""
Module containing the serialize and deserialize functions.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes the dictionary and saves it to json file.

    Args:
    @data: The dictionary to serialize.
    @filename: The json file to write to.

    Return:
    None
    """

    try:
        with open(filename, 'x', encoding='utf-8') as f:
            f.write(json.dumps(data))
    except FileExistsError:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data))


def load_and_deserialize(filename):
    """Deserializes the json file and returns it as a dictionary.

    Args:
    @filename: The json file to read from.

    Return:
    The deserialized dictionary.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
