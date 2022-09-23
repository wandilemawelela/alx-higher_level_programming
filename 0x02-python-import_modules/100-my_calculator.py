#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    operand = ['+', '-', '*', '/']
    if len(sys.argv) == 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        exit(1)
    elif sys.argv[2] not in operand:
        print("Unknown operator. Available operators: +, -, * and /", end="\n")
        exit(1)
    else:
        a, b = int(sys.argv[1]), int(sys.argv[3])
        if sys.argv[2] == operand[0]:
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif sys.argv[2] == operand[1]:
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif sys.argv[2] == operand[2]:
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif sys.argv[2] == operand[3]:
            print("{} / {} = {}".format(a, b, div(a, b)))
