#!/usr/bin/python3

"""
script that takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id
the first argument is your username
the second argument is your password(PAT)
"""

import requests
import sys

if __name__ == "__main__":
    req = requests.get("https://api.github.com/user",
                       auth=(sys.argv[1], sys.argv[2]))
    respons = req.json()
    print(respons.get("id"))
