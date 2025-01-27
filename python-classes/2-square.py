#!/usr/bin/python3
"""
Module for the Square class.
"""


class Square():
    """
    A class defining Square
    Attributes:
        size (int): Private attribute contianing the length of a side
        on the square.
    """

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
