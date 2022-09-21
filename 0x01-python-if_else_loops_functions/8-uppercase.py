#!/usr/bin/python3
def uppercase(str):
    str = ""
    for ch in str:
        if 97 <= ord(ch) <= 122:
            x = ord(ch) - 32
            y = char(x)
            str = str + y
    print("{:s}".format(str))
