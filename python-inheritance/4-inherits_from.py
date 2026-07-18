#!/usr/bin/python3
"""
Module 4-inherits_from
Defines a function that checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class
    (directly or indirectly), otherwise False

    Args:
        obj: the object to check
        a_class: the class to compare against

    Returns:
        True if obj is an instance of a subclass of a_class,
        otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
