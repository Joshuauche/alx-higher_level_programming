#!/usr/bin/python3

"""
script that takes in a URL,
sends a request to the URL and 
displays the body of the response (decoded in utf-8).

manage urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code
"""
from sys import argv
from urllib import request
from urllib.error import HTTPError

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        try:
            response
        except HTTPError as e:
            print(e.read)
            print("Error code: {}".format(e.code))
