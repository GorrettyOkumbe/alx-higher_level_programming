#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        if isinstance(x, list):
            if len(x) == 0:
                print("")
        for y in x:
            if x.index(y) == len(x) - 1:
                print(" {:d}".format(y))
            else:
                print(" {:d}".format(y), end="")
