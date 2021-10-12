#!/usr/bin/python3
"""
object is an instance of a class that inherited
(directly or indirectly) from the specified class
methods:
inherits_from
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the
    specified class ; otherwise False
    :param obj:
    :param a_class:
    :return: True of False
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
