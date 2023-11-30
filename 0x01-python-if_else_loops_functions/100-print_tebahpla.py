#!/usr/bin/python3
for i in range(25, -1, -1):
    c = i + 65
    if i % 2 == 1:
        c += 32
    print("{:c}".format(c), end="")
