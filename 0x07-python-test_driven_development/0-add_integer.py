#!/usr/bin/python3
"""
Sample test cases with doctest.
"""


def add_integer(a, b=98):
    """
    this function adds two integer and float
    :param a: a
    :param b: b
    :return: a + b
    """
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)
