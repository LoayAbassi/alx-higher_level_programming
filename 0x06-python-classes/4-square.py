#!/usr/bin/python3
"""
4-square.py

Description:
    This module defines a Square class with a private instance
    attribute `size`,methods to initialize the size,
    calculate the area, and manage the size attribute
    using property decorators.
"""



class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square. It is a private attribute.

    Methods:
        __init__(self, size=0): Initializes the square with a given size.
        area(self): Calculates the area of the square.
        size(self): Gets the size of the square.
        size(self, value): Sets the size of the square.
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

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
