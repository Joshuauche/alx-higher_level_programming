#!/usr/bin/python3

"""
script that takes in a URL, 
sends a request to the URL and displays 
the body of the response.

If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
"""
from requests.exceptions import HTTPError
import requests
import sys

if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        print(req.text)
    except HTTPError as e:
        print("Error code: {}".format(e.response.text))
