#!/usr/bin/python3
"""
This module defines a Square class with validation and area method.
"""


class Square:
    """
    Square class that defines a square by:
    - Private instance attribute: size
    - Instantiation with optional size (default = 0)
    - Validation: size must be an integer >= 0
    - Public instance method: area()
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size * self.__size
