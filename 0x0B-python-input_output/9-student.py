#!/usr/bin/python3
"""
Defining Class
methods:
def to_json(self):
def __init__(self, first_name, last_name, age):
"""


class Student:
    """
    Class that defines a student by
    some public instance attributes
    """
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of giving parameters
        :param first_name:
        :param last_name:
        :param age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Public method that retrieves a dictionary
        :return: dictionary representation of a Student
        """
        return self.__dict__
