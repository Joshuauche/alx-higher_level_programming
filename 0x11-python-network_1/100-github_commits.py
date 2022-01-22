#!/usr/bin/python3

"""
The first argument will be the repository name
The second argument will be the owner name
You must use the GitHub API,
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
Please list 10 commits
"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get("https://developer.github.com/repos/{}/{}/commits/"
                       .format(sys.argv[1], sys.argv[2]))
    resp = req.json()

    for i in resp[:10]:
        print(i.get('sha'), end=": ")
        print(i.get('commit').get('author').get('name'))
