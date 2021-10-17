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

    json_obj = json.dumps(my_obj)

    with open(filename, mode='w') as a_file:
        a_file.write(json_obj)
