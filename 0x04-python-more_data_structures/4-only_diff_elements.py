#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = set()
    for i in set_1:
        if i in not set_2:
            res.add(i)
    return (res)
