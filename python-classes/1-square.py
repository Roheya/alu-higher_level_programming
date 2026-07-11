#!/usr/bin/python3
"""
This module defines a Square class.
"""
class Square:
    """
    Square class that defines a square by:
    - Private instance attribute: size
    - Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        self.__size = size
