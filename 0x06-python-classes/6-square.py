#!/usr/bin/python3
"""
1-square.py

Description:
    This module defines a Square class with private instance 
    attributes `size` and `position`,
    methods to initialize the size and position,
    calculate the area, manage the size and position
    attributes using property decorators, and print the square.
"""



class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square. It is a private attribute.
        __position (tuple): The position of the square.
                            It is a private attribute.

    Methods:
        __init__(self, size=0, position=(0, 0)):Initializes the square
                                        with a given size and position.
        area(self): Calculates the area of the square.
        size(self): Gets the size of the square.
        size(self, value): Sets the size of the square.
        position(self): Gets the position of the square.
        position(self, value): Sets the position of the square.
        my_print(self): Prints the square using `#` characters.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).

        Raises:
            TypeError: If `size` is not an integer or `position` is not a
                tuple of 2 positive integers.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2 or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

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

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """
        Prints the square using `#` characters. If the size is 0,
        it prints an empty line.
        The square is printed with the specified position
        (leading spaces and new lines).

        """
        if self.__size == 0:
            print()
        else:
            for p in range(self.position[1]):
                print()
            for height in range(self.size):
                print(" " * self.position[0], end="")
                for width in range(self.size):
                    print("#", end="")
                print()
