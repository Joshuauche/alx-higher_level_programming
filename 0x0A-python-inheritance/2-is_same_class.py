#!/usr/bin/python3
"""
Instance of a specified class
methods:
is_same_class
"""


def is_same_class(obj, a_class):
    """
    function that checks if object
    is of same class
    and returns true or false
    :return: True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
