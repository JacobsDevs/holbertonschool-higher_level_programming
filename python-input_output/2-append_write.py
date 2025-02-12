#!/usr/bin/python3
"""
Module containing the append_write function
"""


def append_write(filename="", text=""):
    """Appends text to the file specified.
    Will create file where none exists

    Args:
    @filename: Name of the file to write to.
    @text: The text to write to the file.

    Return:
    The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
