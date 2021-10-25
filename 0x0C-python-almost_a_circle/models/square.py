#!/usr/bin/python3
"""
Square is a special Rectangle
methods:
def __init__(self, size, x=0, y=0, id=None):
def __str__(self):
"""
from typing import Sized
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation of Square class attributes
        :param size:
        :param x:
        :param y:
        :param id:
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Returns the formatted string representation
        of the square class
        :return:
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.__height)

    @property
    def size(self):
        """
        returns the height of the square
        :return:
        """
        return self.__height

    @size.setter
    def size(self, value):
        """
        Assigning with and height to the same value
        :return:
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        self.__height = value
