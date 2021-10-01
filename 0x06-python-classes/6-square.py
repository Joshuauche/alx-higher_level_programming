#!/usr/bin/python3
"""module documentation"""


class Square:
    """Defines a square.
        Private instance attribute: size.
        Instantiate with optional size.
        """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the data conditions"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        else:
            self.__size__ = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position__ = position

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

    @property
    def position(self):
        """Retrieve the position."""
        return self.__position__

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position__ = value

    def area(self):
        """Return the current square area."""
        return self.__size__ ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size__ == 0:
            print()
            return
        for i in range(0, self.__position__[1]):
            print()

        for i in range(0, self.__size__):
            for j in range(0, self.__position__[0]):
                print(" ", end="")
            for x in range(0, self.__size__):
                print("#", end="")
        print()
