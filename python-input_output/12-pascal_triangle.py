#!/usr/bin/python3
"""
Module containing the pascal_triangle function.
"""


def pascal_triangle(n):
    """Pascals Triangle:
    Rules:
        - the first and last element are always 1
        - an element is equal to the sum of its 2 parents

    Args:
    @n: Depth of the triangle to return.

    Return:
    A matrix representing Pascals Triangle.
    """

    array = []
    for i in range(n):
        if array == []:
            array.append([1])
            continue
        else:
            iteration = [x for x in array[i - 1]]
            iteration.append(1)
            temp = [x for x in iteration]
            for c, v in enumerate(iteration):
                if c > 0 and c + 1 < len(iteration):
                    iteration[c] = v + temp[c - 1]
            array.append(iteration)
    return array
