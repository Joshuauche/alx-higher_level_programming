#!/usr/bin/python3
"""
dictionary description with simple data structure
methods:
def class_to_json(obj)
"""


def class_to_json(obj):
    """
    function that returns dictionary
    :param obj:
    :return: dictionary description with simple data structure
    """
    return obj.__dict__
