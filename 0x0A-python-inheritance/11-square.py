#!/usr/bin/python3
"""
Defining the Square class
Method:
__init(self)
area()
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):

    def __init__(self, size):
        """
        Instantiation with size
        :param size:
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Implementing area method
        :return: are of a square
        """
        return self.__size ** 2

    def __str__(self):
        """
        string method
        :return: rectangle description
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
