#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for row in arr:
            if row % 3 == 0:
                print("{:d}".format(row), end="")
            else:
                print("{:d} ".format(row), end="")
        print("")
