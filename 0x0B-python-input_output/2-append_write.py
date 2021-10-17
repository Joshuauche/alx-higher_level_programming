#!/usr/bin/python3
"""
Appends text to a file
Creates it, if doesn't exist
"""


def append_write(filename="", text=""):
    """
    Appends text to a file and returns the text
    :param filename:
    :param text:
    :return:return the text appended and the number of cha
    """

    with open(filename, encoding='utf-8', mode='a')as a_file:
        a_file.write(text)
        return a_file.tell()
