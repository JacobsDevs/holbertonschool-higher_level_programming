"""
Module containing the VerboseList class
"""


class VerboseList(list):
    """
    VerboseList class to override list functions with notifications.
    """

    def append(self, value):
        super().append(value)
        print("Added [{}] to the list.".format(value))

    def extend(self, amount):
        super().extend(amount)
        length = len(amount)
        print("Extended the list with [{}] items.".format(length))

    def remove(self, value):
        try:
            super().remove(value)
            print("Removed [{}] from the list.".format(value))
        except ValueError:
            raise ValueError("Unable to remove {}".format(value))

    def pop(self, index=-1):
        print("Popped [{}] from the list.".format(index))
        return super().pop(index)

