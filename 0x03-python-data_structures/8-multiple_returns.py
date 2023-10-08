#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        return None, None
    else:
        str_len = len(sentence)
        frst_chr = sentence[0]
        return str_len, frst_chr
