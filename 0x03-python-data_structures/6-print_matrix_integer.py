#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for row in arr:
            print("{:d}".format(row), end="") \
                if row == 3 or row == 6 or row == 9 \
                else print("{:d} ".format(row), end="")
        print("")
