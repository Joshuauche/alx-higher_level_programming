#!/usr/bin/python3
"""
available attributes.
methods of an object.
"""


def lookup(obj):
    """
    function that returns the list of available
    attributes and methods of an object:
    :param obj:
    :return: list of objects
    """
    return dir(obj)
