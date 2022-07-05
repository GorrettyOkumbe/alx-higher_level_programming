#!/usr/bin/python3
"""1-write module"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, "w", encoding="utf-8") as file:
        write_data = file.write(text)
        return write_data
