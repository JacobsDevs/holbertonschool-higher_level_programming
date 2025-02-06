"""
Module containing the FlyingFish class
"""


class Fish():
    """
    The Fish class
    """


    def swim(self):
        print("The {} is swimming!".format(self.__class__.__name__))

    def habitat(self):
        print("The {} lives in water".format(self.__class__.__name__))


class Bird():
    """
    The Bird class
    """

    def fly(self):
        print("The {} is soaring!".format(self.__class__.__name__))

    def habitat(self):
        print("The {} lives in the sky".format(self.__class__.__name__))


class FlyingFish(Fish, Bird):
    """
    The FlyingFish class
    """
    def __init__(self):
        self.__class__.__name__ = "flying fish"

    def habitat(self):
        print("The {} lives both in water and the sky!".format(self.__class__.__name__))
