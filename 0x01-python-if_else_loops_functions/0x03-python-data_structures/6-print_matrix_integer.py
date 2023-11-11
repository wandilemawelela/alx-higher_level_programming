#!/usr/bin/python3
def print_matrix_integer(matrix=None):
    if matrix is None:
        return

    if not matrix:
        return

    for arr in matrix:
        if not arr:
            continue

        for i, row in enumerate(arr):
            if i == len(arr) - 1:
                print("{:d}".format(row))
            else:
                print("{:d} ".format(row), end="")
