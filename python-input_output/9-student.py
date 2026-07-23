#!/usr/bin/python3
"""
Class Student that defines a student by:
- Public instance attributes: first_name, last_name, age
- Instantiation with first_name, last_name and age
- Public method to_json() that retrieves a dictionary representation
"""
class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of Student instance"""
        return self.__dict__
