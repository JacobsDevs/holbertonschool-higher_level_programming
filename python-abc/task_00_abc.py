#!/usr/bin/python3
"""
Module containing the abstract class Animal.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal class inherits ABC
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Dog class inherits from Animal

    Abstract Methods:
        sound(): a dog will Bark
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat class ingerits from Animal

    Abstract Methods:
        sound(): a cat will Meow
    """

    def sound(self):
        return "Meow"
