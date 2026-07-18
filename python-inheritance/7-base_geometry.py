#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with area and integer validation methods
"""


class BaseGeometry:
    """
    BaseGeometry class
    Provides a foundation for geometry classes with validation
    """

    def area(self):
        """
        Raises an Exception since area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0

        Args:
            name (str): the name of the value
            value (int): the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
