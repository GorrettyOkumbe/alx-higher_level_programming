#!/usr/bin/python3
def max_integer(my_list=[]):
    new_list = sorted(my_list)
    if len(my_list) == 0:
        return None
    else:
        return new_list[-1]
