#!/usr/bin/python3
"""
Module containing the Shape abstract class as well as the Circle and Rectangle
classes.

Functions:
shape_info - exhibits ducktyping through Circle and Rectangle classes.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    abstract class Shape
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    class Circle that inherits from Shape
    """

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
    class Rectangle that inherits from Shape
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (2 * self.__width) + (2 * self.__height)


def shape_info(shape):
    try:
        print("Area: {}". format(shape.area()))
        print("Perimeter: {}". format(shape.perimeter()))
    except Exception:
        print("Unable to provide shape info")

