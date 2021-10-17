#!/usr/bin/python3
"""
Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
     function that creates an Object from a JSON file
    :param filename:
    :return: the creted JSON object
    """
    with open(filename, mode='r') as a_file:
        return json.load(a_file)
