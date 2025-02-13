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

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(
                isinstance(elem, str) for elem in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        else:
            return self.__dict__

    def reload_from_json(self, json: dict):
        vars(self).update(json)
