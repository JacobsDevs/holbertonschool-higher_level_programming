"""
Module containing the Dragon class and the Swim and Fly Mixins
"""


class SwimMixin():
    """
    Mixin to give a class a swim function
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin():
    """
    Mixin to give a class a fly function
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    The Dragon class
    """

    def roar(self):
        print("The dragon roars!")
