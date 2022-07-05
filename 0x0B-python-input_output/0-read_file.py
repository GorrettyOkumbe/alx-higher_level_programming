#!/usr/bin/python3
"""0-read_file module"""


def read_file(filename=""):
    """reads from a text file"""

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
