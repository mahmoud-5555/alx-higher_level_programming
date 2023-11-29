#!/usr/bin/python3
def islower(c):
    if ord(c) >= 32 and ord(c) <= 125:
        if c >= 'a' and c <= 'z':
            return (True)
        else:
            return (False)
    else:
        print("Traceback (most recent call last):")
