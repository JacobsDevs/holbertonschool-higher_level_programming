#!/usr/bin/python3
"""This is the 4-print_square module which contains the print_square function:
Args:
    size: The height and width of the square to print.
"""


def print_square(size):
    """
    Prints a square of the desired height.
    """
    try:
        if size < 0:
            raise ValueError
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
    except ValueError:
        if isinstance(size, float):
            raise TypeError('size must be an integer')
        else:
            raise ValueError('size must be >= 0')
    except TypeError:
        raise TypeError('size must be an integer')
