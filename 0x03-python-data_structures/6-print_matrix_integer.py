#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for row in arr:
            print("{:d}".format(row), end="") \
                    if row % 3 == 0 else print("{:d} ".format(row), end="")
        print("")
