#!/usr/bin/python3
"""
Defines a class Myint
methods:
__eq__(self, other)
__ne__(self, other)
"""


class MyInt(int):
    """
    Inherits the class int
    """

    def __eq__(self, other):
        """
        Inbuilt method used for equality sign
        :param other:
        :return: inverted operator
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inbuilt method used for not equal to sign
        :param other:
        :return: inverted operator
        """
        return super().__eq__(other)
