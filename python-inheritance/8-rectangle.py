#!/usr/bin/python3
"""
This is the module containing the Rectangle class.
This class inherits from the BaseGeometry class located in 7-base_geometry.py
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The Rectangle class
    Inherits:
        BaseGeometry

    Args:
        @width: Length of the horizontal sides.
        @height: Length of the vertical sides.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
