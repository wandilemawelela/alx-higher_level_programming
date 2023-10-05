#!/usr/bin/python3
#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:  # When there are 0 args
        print("0 arguments.", end="\n")
    elif len(sys.argv) == 2:  # When there is 1 arg
        print("1 argument:", end="\n")
        print("1: {}".format(sys.argv[1]), end="\n")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1), end="\n")
        for i in range(1, len(sys.argv)):
            print("{:d}: {}".format(i, sys.argv[i]), end="\n")
