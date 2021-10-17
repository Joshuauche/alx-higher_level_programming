#!/usr/bin/python3
"""
 From JSON string to Object
"""
import io
import json


def from_json_string(my_str):
    """
    Object represented by a JSON string
    :param my_str:
    :return:JSON string
    """
    return json.loads(my_str)
