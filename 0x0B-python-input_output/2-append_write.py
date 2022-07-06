#!/usr/bin/python3
"""2-append module"""


def append_write(filename="", text=""):
    """writes to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        write_data = file.write(text)
        return write_data
