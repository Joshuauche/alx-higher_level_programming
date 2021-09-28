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
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size__ = value

    def area(self):
        """Return the current square area."""
        return self.__size__ ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size__ == 0:
            print()
        else:
            for i in range(0, self.__size__):
                for j in range(0, self.__size__):
                    print("#", end="")
                print()
