#!/usr/bin/python3
"""
This is the base_geometry module containing the BaseGeometry class
"""


class BaseGeometry():
    """
    BaseGeometry class
    """
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int):
            if value <= 0:
                error = "{} must be greater than 0".format(name)
                raise ValueError(error)
            self.name = value
        else:
            error = "{} must be an integer".format(name)
            raise TypeError(error)
