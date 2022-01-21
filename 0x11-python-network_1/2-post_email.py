#!/usr/bin/python3

"""
script that takes aurl and an email,
sends POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request as request
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":
    d_email = {'email': argv[2]}
    data = parse.urlencode(d_email).encode('utf-8')
    with request.urlopen(argv[1], data=data) as response:
        resp = response.read()
        print(resp.decode("utf-8"))
