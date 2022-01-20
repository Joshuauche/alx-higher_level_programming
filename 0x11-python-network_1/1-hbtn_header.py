#!/usr/bin/python3
import urllib.request
from sys import argv

"""
script that takes in a URL,
ends a request to the URL and displays the value of the X-Request-Id
variable found in the header of the response
"""

with urllib.request.urlopen(argv[1]) as response:
    print(response.getheader("X-Request-Id"))
