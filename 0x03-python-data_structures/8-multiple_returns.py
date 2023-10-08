#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        sentence[0] = None
    else:
        str_len = len(sentence)
        frst_chr = sentence[0]
        return str_len, frst_chr
