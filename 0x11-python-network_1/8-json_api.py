#!/usr/bin/python3

"""
script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
display the id and name like this: [<id>] <name>

Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        set_q = {"q": ""}
    else:
        set_q = {"q": sys.argv[1]}
    req = requests.post("http://0.0.0.0:5000/search_user", data=set_q)
    try:
        respons = req.json()
        if respons != {}:
            print("[{}] {}".format(respons["id"], respons["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
