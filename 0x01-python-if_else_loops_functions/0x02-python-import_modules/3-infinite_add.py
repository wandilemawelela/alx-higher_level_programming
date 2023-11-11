#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0", end="\n")
    else:
        del sys.argv[0]
        print("{}".format(sum(map(int, sys.argv))))
