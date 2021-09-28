#!/usr/bin/python3
class Square:
    """Defines a square.
    Private instance attribute: size.
    Instantiate with optional size.
    """
    def __init__(self, size=0):
        """Initialize the data conditions"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size__ = size
