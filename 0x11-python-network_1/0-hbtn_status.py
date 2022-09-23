#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
must use the package urllib and with statement
The body of the response must be displayed like \
        likethe following example (tabulation before -)
You are not allowed to import any packages other than urllib
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
