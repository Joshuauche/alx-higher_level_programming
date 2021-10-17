#!/usr/bin/python3
"""
Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation:
    :param my_obj:
    :param filename:
    :return: JSON represntations
    """

    with open(filename, mode='w') as a_file:
        json_obj = json.dumps(my_obj)
        a_file.write(json_obj)
