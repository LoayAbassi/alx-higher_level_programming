#!/usr/bin/python3
"""
6-rectangle.py
Description:
This module contains a class that defines a rectangle with
getters and setters for the width and height.
perimeter and area claculation, along with string representation.
and possibility to recreate the instance using eval()
counts number of times the class was initialized
"""


class Rectangle:
    """
    A simple class that defines a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances(int): increments each call of Rectangle.
    Methods:
        area() ->int: Calculates the area of the rectangle.
        perimeter() ->int: Calculates the perimeter of the rectangle.
        __str__() ->str: Returns a string representation of the rectangle.
        __repr__() ->str: Returns a string representation of the rectangle
                        that can be used to recreate the instance.
        __del__() : prints a message when rectangle destroyed """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
            Returns 0 if either width or height is 0.

        """
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        returns a rectangle with # character.
        """
        x = ""
        if not (self.height == 0 or self.width == 0):
            for i in range(self.height):
                x = x+"#"*self.width+"\n"
        return x[:len(x)-1]

    def __repr__(self):
        """returns a representation of the object"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """prints a message when rectangle is destroyed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
