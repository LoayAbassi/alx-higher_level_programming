#!/usr/bin/python3
"""
1-square.py

Description:
    This module defines a Square class with a private instance attribute `size`
    and methods to initialize the size and calculate the area of the square.
"""

class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square. It is a private attribute.

    Methods:
        __init__(self, size=0): Initializes the square with a given size.
        area(self): Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
