#!/usr/bin/python3
"""
To JSON string
"""
import json


def to_json_string(my_obj):
    """
    JSON representation of an object
    :param my_obj:
    :return: JSON object
    """
    return json.dumps(my_obj)
