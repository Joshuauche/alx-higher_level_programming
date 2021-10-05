#!/usr/bin/python3
"""Define the height and width of a rectangle"""


class Rectangle:
    """Defines a rectangle.
        Private instance attribute: width.
        Instantiate with optional height.
    """
    def __init__(self, width=0, height=0):
        """Initialize the data conditions"""
        self.__width__ = width
        self.__height__ = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width__

    @width.setter
    def width(self, value):
        """Sets the width to a value."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width__ = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height__

    @height.setter
    def height(self, value):
        """Sets the height to a value."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height__ = value
