#!/usr/bin/python3
def no_c(my_string):
    return my_string.translate({ord('C'): None}) \
        if 'C' in my_string else my_string.translate({ord('c'): None})
