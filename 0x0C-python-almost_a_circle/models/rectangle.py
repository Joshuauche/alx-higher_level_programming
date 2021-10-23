#!/usr/bin/python3
"""
class Rectnagle inherits from class Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Inherits from class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Difinition of instantiation parameters
        :param width:
        :param height:
        :param x:
        :param y:
        :param id:
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Retrieves the width
        :return: private width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Modifies the width value
        :param value:
        :return: return modified width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height
        :return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Modifies the height value
        :param value:
        :return: height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__width = value

    @property
    def x(self):
        """
        Retrieves the x
        :return: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Modifies x
        :param value:
        :return: x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """
        Retrieves the y
        :return: private y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Modifies the value
        :param value:
        :return: value y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value
