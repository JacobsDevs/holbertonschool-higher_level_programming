#!/usr/bin/python3
"""
Module containing the CustomObject class.
"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student) -> None:
        self.name: str = name
        self.age: int = age
        self.is_student: bool = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
        except pickle.UnpicklingError:
            return None
        except EOFError:
            return None
