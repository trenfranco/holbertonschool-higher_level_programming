#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    a = 0
    for i in new:
        a = a + i
    return a
