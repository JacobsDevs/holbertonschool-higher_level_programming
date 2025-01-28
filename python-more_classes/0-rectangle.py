#!/usr/bin/python3

"""
Module containing the rectangle class.
"""


class Rectangle():
    """
    Rectangle Class definition
    """

    def __init__(self, height=0, width=0):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
