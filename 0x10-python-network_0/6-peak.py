#!/usr/bin/python3
"""
finds the peak in a list of unsortef integers
"""


def find_peak(list_of_integers):
    """
    function to find the peak value
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
