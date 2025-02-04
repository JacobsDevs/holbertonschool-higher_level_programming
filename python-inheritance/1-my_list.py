#!/usr/bin/python3
"""
This is the module 1-my_list that contains the MyList class.
"""


class MyList(list):
    """
    class MyList:

    Inherits: List

    methods:
    print_sorted:
        prints the list in a sorted format.
    """

    def print_sorted(self):
        print(sorted(self))
