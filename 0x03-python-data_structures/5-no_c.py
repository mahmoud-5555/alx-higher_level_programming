#!/usr/bin/python3
    no_c(my_string):
    res = ''
    for i in my_string:
        if i != 'c' and i != 'C':
           res += i
    return res