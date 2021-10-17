#!/usr/bin/python3
"""
Writtes to a file and returns the number of string
"""


def write_file(filename="", text=""):
    """
    Returns the number of characters
    Creates the file if it doesn't exist
    Write to the file
    :param filename:
    :param text:
    :return: the number od strings
    """

    with open(filename, encoding='utf-8', mode='w') as a_file:
        a_file.write(text)
        return a_file.tell()
