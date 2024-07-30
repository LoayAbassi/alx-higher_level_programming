#!/usr/bin/python3
"""
    module contains a function that devides a matrix's elements 
    after checking for some specific conditions.
    """


def matrix_divided(matrix, div):
    """Divide each element of a matrix by a given number.
    Args:
    matrix (list): A 2D list of numbers.
    div (int or float): The number to divide each element by.
    Returns:
    list: A new 2D list with each element divided by the given number.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if not (isinstance(i, list) and len(i) != 0):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for e in i:
            if not isinstance(e, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    return [[round(element/div, 2) for element in row]for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
