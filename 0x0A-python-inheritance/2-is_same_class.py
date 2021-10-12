#!/usr/bin/python3
"""
Instance of a specified class
methods:
is_same_class
"""


def is_same_class(obj, a_class):
    """
    checks if object is of same class
    :param obj: obj
    :param a_class: a_class
    :return: True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
