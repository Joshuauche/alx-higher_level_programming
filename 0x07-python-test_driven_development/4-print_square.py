#!/usr/bin/python3
"""
Defines a function that prints a square using #
"""


def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise "size must be an integer"
    else:
        for row in range(0, size):
            for i in range(0, size):
                print("#", end="")
            print()
