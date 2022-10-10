#!/usr/bin/python3
def safe_print_division(a, b):

    try:
        value = a / b
        return value
    except ZeroDivisionError:
        value = None
        return value
    finally:
        print("Inside result: {}".format(value))
