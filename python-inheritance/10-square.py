#!/usr/bin/python3
"""
Module 10-square
Defines a Square class that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initialize Square with validated size

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is <= 0
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the square description in the format:
        [Square] <size>/<size>
        """
        return f"[Square] {self.__size}/{self.__size}"
