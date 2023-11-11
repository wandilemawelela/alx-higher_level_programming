#!/usr/bin/python3
if a < b:
    c = add(a, b)

    for i in range(4, 6):
        c = add(c, i)
        return c
else:
    return sub(a, b)
