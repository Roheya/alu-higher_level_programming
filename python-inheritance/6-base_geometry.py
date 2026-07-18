#!/usr/bin/python3
"""
Module 6-base_geometry
Defines a class BaseGeometry with an unimplemented area method
"""


class BaseGeometry:
    """
    BaseGeometry class
    Provides a foundation for geometry classes
    """

    def area(self):
        """
        Raises an Exception since area is not implemented
        """
        raise Exception("area() is not implemented")
