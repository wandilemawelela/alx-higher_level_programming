#!/usr/bin/python3
for num in range(00, 100):
    print("{:02d}".format(num), end='' if num == 99 else ", ")
