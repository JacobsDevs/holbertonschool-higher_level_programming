#!/usr/bin/python3
"""
Module containing the write_file function
"""


def write_file(filename="", text=""):
    """Writes text to the file specified.  Will overwrite existing file.
    Will create file where none exists

    Args:
    @filename: Name of the file to write to.
    @text: The text to write to the file.

    Return:
    None
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
