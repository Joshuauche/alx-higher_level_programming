#!/usr/bin/python3
"""
Defining the Square class
Method:
__init(self)
area()
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
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
        Implementing area method
        :return: are of a square
        """
        return self.__size ** 2

    def __str__(self):
        """
        string method
        :return: rectangle description
        """
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
