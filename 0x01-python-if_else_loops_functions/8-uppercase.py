#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ch in str:
        if "a" <= ch <= "z":
            ch = chr(ord(ch) - 32)
        result += ch
    print(result)
