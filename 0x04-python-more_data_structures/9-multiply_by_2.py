#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = dict(a_dictionary)
    for key in a:
        a[key] = a[key] * 2
    return a

