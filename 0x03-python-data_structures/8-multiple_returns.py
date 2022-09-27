#!/usr/bin/python3
def multiple_returns(sentence):
    length, first = len(sentence), sentence[0]
    return None if sentence == " " else length, first
