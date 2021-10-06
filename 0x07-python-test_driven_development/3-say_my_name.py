#!/usr/bin/python3
"""
Defines a function that prints two names
"""


def say_my_name(first_name, last_name=""):
    """
    prints first name and last name
    :param first_name: first name
    :param last_name: last name
    :return: first name and last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
