#!/usr/bin/python3
"""
Base class fo all other classes
methods:
def __init__(self, id=None):
"""


class Base:
    """
    Private class atrribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
