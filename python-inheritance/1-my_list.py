#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list
"""


class MyList(list):
    """
    MyList class that inherits from list
    Provides an additional method to print the list in sorted order
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        The original list remains unchanged
        """
        print(sorted(self))
