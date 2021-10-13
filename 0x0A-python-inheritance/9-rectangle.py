#!/usr/bin/python3
"""
Defining BaseGeometry class
methods:
__init__(self)

"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits from class BaseGeometry
    """

    def __init__(self, width, height):
        """
        validates positive integer using integer_validation method
        private width and height
        :param width:
        :param height:
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        implementing area method
        :return: area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        string method
        :return: rectangle description
        """
        return "[Rectangle] {} / {}".format(self.__width, self.__height)
