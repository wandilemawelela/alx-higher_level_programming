#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        row_str = " ".join(
            str(row) if row % 3 != 0 else str(row) for row in arr
        )
        print(row_str)
