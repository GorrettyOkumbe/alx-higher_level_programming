#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):  # first check if it is a list
        for i in my_list[::-1]:  # then iterate through and reverse the list
            print("{:d}".format(i))
