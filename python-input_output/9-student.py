#!/usr/bin/python3
"""
Module containing the Student class.
"""


class Student:
    """The student class has a first and last name as well as an age.
    """

    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
