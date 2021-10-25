#!/usr/bin/python3
"""
Square is a special Rectangle
methods:
def __init__(self, size, x=0, y=0, id=None):
def __str__(self):
"""
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
                                                 self.height)
