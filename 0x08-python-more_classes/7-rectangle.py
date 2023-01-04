#!/usr/bin/python3
"""Defines a Rectangular class."""

class Rectangle:
    """represent a rectangle.

    Attributes:
    number of instances (int): The number of rectangle instances.
    print_symbol (any): the symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
        width (int): The width of the new rectangle.
        height (int): The height of the rectangle.
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
            self.__width = value
            
            @property
            def height(self):
                """Get/set the height of the rectangle."""
                return self.__width
    
            @height.setter
            def height(self, value):
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value




