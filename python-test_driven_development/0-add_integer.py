#!/usr/bin/python3
"""This is the 0-add_integer module which contains the add_integer file:
Args:
    a: The first integer to be added.
    b: The second integer to be added.
Return:
    The result of a + b
"""


def add_integer(a, b=98):
    """
    Return the result of a + b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if abs(a)==float('inf'):
        raise OverflowError("float is overflowing")
    try:
        return int(a) + int(b)
    except ValueError:
        pass
