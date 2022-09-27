#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == " ":
        first = None
        return first
    else:
        length, first = len(sentence), sentence[0]
        return length, first
