#!/usr/bin/python3
"""
Defining Class
methods:
def to_json(self):
def __init__(self, first_name, last_name, age):
def reload_from_json(self, json):
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

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary
        :return: dictionary representation of a Student
        """
        if attrs is None:
            return self.__dict__

        json_dict = {}
        for i in attrs:
            if hasattr(self, i):
                json_dict[i] = getattr(self, i)
        return json_dict

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        :param json:
        :return: the attribute of each key value pair
        """
        for key, value in json.items():
            setattr(self, key, value)
