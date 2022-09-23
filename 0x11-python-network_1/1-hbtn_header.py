#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL
 displays the value of the X-Request-Id variable
 found in the header of the response.
"""
import sys
import urllib.request
if __name__ == "__main__":
    args = sys.argv[1]
    with urllib.request.urlopen(args) as res:
        print(dict(res.headers).get("X-Request-Id"))
