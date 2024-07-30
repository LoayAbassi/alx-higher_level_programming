#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers. Casts floats to integers.

    Raises:
        TypeError: If a or b is neither an integer nor a float.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a,(int,float)):
        raise TypeError("a must be an integer")
    if not isinstance(b,(int,float)):
        raise TypeError("b must be an integer")
    return a+b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests\0-add_integer.txt")
