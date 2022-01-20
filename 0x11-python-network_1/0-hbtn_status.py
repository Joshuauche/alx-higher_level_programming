#!/usr/bin/python3
import urllib.request
"""
script that fetches, using urllib
"""
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    if response.readable():
        resp = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(resp)))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(resp.decode("UTF-8")))
