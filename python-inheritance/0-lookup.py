#!/usr/bin/python3
"""
Module 0-lookup
Defines a function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object

    Args:
        obj: the object to inspect

    Returns:
        A list of attributes and methods of the object
    """
    return dir(obj)
