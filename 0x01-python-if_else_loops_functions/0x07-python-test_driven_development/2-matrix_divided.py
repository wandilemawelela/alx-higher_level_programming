#!/usr/bin/python3
"""
This is the matrix_divided module

This module has the matrix_divided()
function that divides every element
of a matrix.
"""


def matrix_divided(matrix, div):
    """ Returns the result of each member of the matrix list
    divided by the div variable. Otherwises raises a TypeError
    if member of the matrix is not an int or float or if each
    row of the matrix does not have the same size. The fucntion
    also returns a ZeroDivisionError if the value of div is 0.
    """

    if not isinstance(matrix, list) or any(not isinstance(row, list)
                                           for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
