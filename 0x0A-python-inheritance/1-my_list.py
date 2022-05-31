#!/usr/bin/python3
"""new class"""


class MyList(list):
    """my list class"""
    pass

    def print_sorted(self):
        a = self[:]
        a.sort()
        print(a)
