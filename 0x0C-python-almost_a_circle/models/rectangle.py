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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        if value <= 0:
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
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """
        Public method
        return area value of the rectangle instance
        :return: area of a rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        displays the area of rectangle in hashes
        :return: #
        """
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for j in range(0, self.__x):
                print(" ", end="")
            for k in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        string representation of the rectangle
        to be able to recreate a new instance
        :return:
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args):
        """
        assigns an argument to each attribute:
        :param args:
        :return: assigns an argument
        """
        new_args = [self.id, self.__width, self.__height, self.__x, self.__y]
        if len(args) == 0 or args is None:
            return
        else:
            for i in range(len(args)):
                new_args[i] = args[i]
                self.__init__(new_args[1],
                              new_args[2],
                              new_args[3],
                              new_args[4],
                              new_args[0])
