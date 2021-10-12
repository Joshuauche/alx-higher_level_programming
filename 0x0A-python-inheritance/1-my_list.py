#!/usr/bin/python3
"""
class that inherit from another class
"""


class MyList(list):
    """
    My list class
    method:
    print_sorted
    """

    def print_sorted(self):
        """
        public instance method.
        :return: the sorted list
        """
        print(sorted(self))
