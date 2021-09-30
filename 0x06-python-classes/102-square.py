#!/usr/bin/python3
"""module documentation"""


class Square:
    """Defines a square.
        Private instance attribute: size.
        Instantiate with optional size.
        """
    def __init__(self, size=0):
        """Initialize the data conditions"""
        self.__size__ = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size__

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if type(value) != int or type(value) != float:
            raise TypeError("size must be an number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size__ = value

    def area(self):
        """Return the current square area."""
        return self.__size__ ** 2

    def __lt__(self, other):
        """check for less than comparator"""
        return self.area() < other.area()

    def __gt__(self, other):
        """check for greater than comparator"""
        return self.area() > other.area()

    def __eq__(self, other):
        """check for equal to comparator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """check for not equal to comparator"""
        return self.area() != other.area()

    def __ge__(self, other):
        """check for greater or equal to comparator"""
        return self.area() >= other.area()

    def __lessEqual__(self, other):
        """check for less than or equal comparator"""
        return self.area() <= other.area()
