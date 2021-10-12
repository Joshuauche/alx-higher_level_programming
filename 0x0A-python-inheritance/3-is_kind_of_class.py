#!/usr/bin/python3
"""
object is an instance of,
or if the object is an instance of a
class that inherited from, the specified class
methods:
is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    returns true or false if the object
    is an instance of a class that inherited from
    :param obj:
    :param a_class:
    :return: True or false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
