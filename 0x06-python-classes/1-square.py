#!/usr/bin/python3
"""
1-square.py

Description:
    This module defines a Square class with a
    private instance attribute `size`.
"""


class Square:
    """
    This is a class that represents a square.

    Attributes:
        __size (int): The size of the square, which is private.

    Methods:
        __init__(self, size = 0): initializing the square with a given size.
    """

    def __init__(self, size=0):
        """
        This is the constructor of the Square class
        It initializes the size of the square
        Args:
            size (int): The size of the square
        """
        self.__size = size
