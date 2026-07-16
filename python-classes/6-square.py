#!/usr/bin/python3
"""
This module defines a Square class with validation,
area method, and printing functionality with position.
"""


class Square:
    """
    Square class that defines a square by:
    - Private instance attributes: size, position
    - Instantiation with optional size and position
    - Validation: size must be an integer >= 0
                  position must be a tuple of 2 positive integers
    - Public instance methods: area(), my_print()
    - Property getters and setters for size and position
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#'.
        If size is 0, prints an empty line.
        Position is used to offset the square.
        """
        if self.__size == 0:
            print("")
            return

        # vertical offset
        for _ in range(self.__position[1]):
            print("")

        # horizontal offset + square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
