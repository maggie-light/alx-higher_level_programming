#!/usr/bin/python3
"""Defines a rectangle class."""

class Rectangle:
    """Represent a rectangle.

    Attributes:
    number_of_instances (int): The number of rectangle instances.
    print_symbol (any): the symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
        width (int): the width of the new rectangle.
        height (int): the height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

        @property
        def width(self):
            """Get/set the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            return self.__width = value

        @property
        def height(self):
            """Get/set the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be and integer")
            if value < 0:

                raise ValueError("height must be >= 0")
            return self.__height = value



