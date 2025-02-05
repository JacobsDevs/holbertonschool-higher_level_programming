#!/usr/bin/python3
"""
Module containing the Square class that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square Class that inherits from Rectangle
    (Which inherits from Base Geometry)

    Args:
    @size: The length of a side.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[{}] {}/{}".format(Rectangle.__name__,
                                   self.__size,
                                   self.__size)
