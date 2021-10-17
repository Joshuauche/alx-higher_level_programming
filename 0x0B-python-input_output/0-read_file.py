#!/usr/bin/python3
""""
Read file
functions:
def read_file(filename=""):
"""


def read_file(filename=""):
    """
    Reads from a file and prints
    :param filename:
    :return:
    """
    with open(filename, encoding='utf-8', mode='r') as a_file:
        read_text = a_file.read()
        print(read_text)
