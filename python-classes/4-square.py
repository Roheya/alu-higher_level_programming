#!/usr/bin/python3
"""
This module defines a Square class with validation, area method,
and property access for size.
"""


class Square:
    """
    Square class that defines a square by:
    - Private instance attribute: size
    - Instantiation with optional size (default = 0)
    - Validation: size must be an integer >= 0
    - Public instance method: area()
    - Property getter and setter for size
    """

    def __init__(self, size=0):
        self.size = size  # uses the setter for validation

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size * self.__size
