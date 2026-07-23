#!/usr/bin/python3
"""
Class Student that defines a student by:
- Public instance attributes: first_name, last_name, age
- Instantiation with first_name, last_name and age
- Public method to_json(attrs=None) that retrieves a dictionary
  representation of a Student instance
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of Student instance.
        If attrs is a list of strings, only attributes in this list
        are retrieved. Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
