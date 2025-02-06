"""
Module containing the CountedIterator class.
"""


class CountedIterator():
    """
    Counted Iterator class
    """

    def __init__(self, data):
        self.iterator = iter(data)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        try:
            next(self.iterator)
        except Exception:
            raise StopIteration("No more items")
