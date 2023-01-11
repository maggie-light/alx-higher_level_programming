#!/usr/bin/python3
"""Defines a class rectangle that inherits from BaseGeometry."""
BaseGeomtry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
        widt (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
