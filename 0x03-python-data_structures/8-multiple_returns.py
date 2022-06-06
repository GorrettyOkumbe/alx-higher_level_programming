#!/usr/bin/python3
def multiple_returns(sentence):
    s = sentence
    if s == "":
        return (0, None)
    else:
        return (len(s), s[0])
