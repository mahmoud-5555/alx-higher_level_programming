#!/usr/bin/python3
"""FILE READER"""


def read_file(filename=""):
    """
        function that print the contest that inside the file
    """
    contest = ''
    with open(filename, 'r+', encoding='UTF8') as myfile:
        contest = myfile.read()
        print(contest)
        return contest
