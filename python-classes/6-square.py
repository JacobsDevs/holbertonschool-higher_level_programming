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

    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        if isinstance(position, tuple):
            if (not isinstance(position[0], int) or
                    not isinstance(position[1], int) or
                    position[0] < 0 or
                    position[1] < 0):
                raise TypeError("position must be a tuple of \
                    2 positive integers")
            else:
                self.__position = position
        else:
            raise TypeError("position must be a tuple of \
            2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            if (not isinstance(value[0], int) or
                    not isinstance(value[1], int) or
                    value[0] < 0 or
                    value[1] < 0):
                raise TypeError("position must be a tuple of \
                2 positive integers")
            else:
                self.position = value
        else:
            raise TypeError("position must be a tuple of \
            2 positive integers")
        return self.__size * self.__size

    def my_print(self):
        if self.position[1] > 0:
            for i in range(self.position[1]):
                print("")
        if self.size > 0:
            for i in range(self.size):
                if self.position[0] > 0:
                    for i in range(self.position[0]):
                        print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
        else:
            print("")

    def area(self):
        return self.__size * self.__size
