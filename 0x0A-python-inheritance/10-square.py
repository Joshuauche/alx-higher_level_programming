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
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Implementing the area of square
        :return: area of a sqaure
        """
        return self.__size ** 2

