#!/usr/bin/python3

"""

"""
from requests.exceptions import HTTPError
import requests
import sys

if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        print(req.text)
    except HTTPError as e:
        print("Error code: {}".format(e.errno))