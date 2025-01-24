#!/usr/bin/python3
"""This is the 2-matrix_divided module which contains the matrix_divided function:
Args:
    matrix: The matrix to be divided.
    div: The integer to divide each element of the matrix by.
Return:
    The matrix of results
"""

def matrix_divided(matrix, div):
    """
    Divide each element of the matrix by div and return the new matrix
    """
    correct_length = True
    div_is_number = True
    try:
        new_matrix = list(matrix)
        if not isinstance(div, (int, float)):
            div_is_number = False
            raise TypeError
        for c, v in enumerate(matrix):
            for d, j in enumerate(v):
                new_matrix[c][d] = round(j / div, 2)
        if len(set(map(lambda x: len(x), matrix))) > 1:
            correct_length = False
            raise TypeError
        return new_matrix

    except TypeError:
        if not correct_length:
            raise TypeError('Each row of the matrix must have the same size')
        if not div_is_number:
            raise TypeError('div must be a number')
        else:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
