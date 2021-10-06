#!/usr/bin/python3
"""
Defines a function that indents text
"""


def text_indentation(text):
    """
    prints the text indented sentence
    :param text: 
    :return: indented sentence
    """
    special_char = ['.', '?', ':']
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i in special_char:
            print('\n\n', end="")
