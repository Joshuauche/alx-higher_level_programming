#!/usr/bin/python3
"""
sends a request to the URL
and displays the value of the variable
X-Request-Id in the response header
"""

from webbrowser import get
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    resp = req.headers.get('X-Request-Id')
    print(resp)
