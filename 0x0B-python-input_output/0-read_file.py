#!/usr/bin/python3
"""input output function"""


def read_file(filename=""):
    with open(filename) as a:
        print(a.read())
