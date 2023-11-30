#!/usr/bin/bython3
def remove_char_at(str, n):
    string = ''
    for i, c in enumerate(str):
        if i != n:
            string = string + c
    return (string)
