#!/usr/bin/python3
"""
Defining BaseGeometry class
methods:
area
integer_validator
"""


class BaseGeometry:
    """
    Empty class
    """

    def area(self):
        """
        Raises an exception message
        :return: exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate the parameter value or
        raise type error or value
        :param name:
        :param value:
        :return: value
        """
        self.name = name
        self.value = value
        if type(self.value) is not int:
            raise TypeError("{:s} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{:s} must be greater than 0".format(self.name))
        return value
