#!/usr/bin/python3
def print_last_digit(number):
    last_number = int(repr(number)[-1])
    print("{}".format(last_number), end="")
    return last_number
