#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        new_list = [i for i in my_list[:]]
        if idx > (len(new_list) - 1) or idx < 0:
            return new_list
        new_list[idx] = element
        return new_list
