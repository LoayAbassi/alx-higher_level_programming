#!/usr/bin/python3
"""Module for matrix_mul method."""


def matrix_mul(m_a, m_b):
    """Multiplies one matrix by another.
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        matrix: the product
    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty lists/matrices.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangular.
        ValueError: If m_a or m_b can't be multiplied.
    """
    
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")
    
    if not m_a or not all(isinstance(row, list) for row in m_a) or not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a must be a list of lists containing integers or floats")
    
    if not m_b or not all(isinstance(row, list) for row in m_b) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b must be a list of lists containing integers or floats")

    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[0] * len(m_b[0]) for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            res[i][j] = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
    
    return res



if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
