#!/usr/bin/python3
"""
This module defines a Rectangle class with validation
for width and height, and methods for area, perimeter,
string representation, instance tracking, and customizable
print symbol.
"""


class Rectangle:
    """
    Rectangle class that defines a rectangle by:
    - Private instance attributes: width, height
    - Public class attributes: number_of_instances, print_symbol
    - Instantiation with optional width and height
    - Validation: width and height must be integers >= 0
    - Property getters and setters for width and height
    - Public instance methods: area(), perimeter()
    - __str__ method to print the rectangle using print_symbol
    - __repr__ method to recreate the instance
    - __del__ method to print a message when deleted
    """

    number_of_instances = 0  # class attribute
    print_symbol = "#"       # class attribute, customizable

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        If width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation of the rectangle
        using print_symbol. If width or height is 0,
        return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_lines = []
        symbol = str(self.print_symbol)
        for _ in range(self.__height):
            rect_lines.append(symbol * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Return a string representation of the rectangle
        that can recreate a new instance using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when a Rectangle instance is deleted
        and decrement the number_of_instances counter.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
