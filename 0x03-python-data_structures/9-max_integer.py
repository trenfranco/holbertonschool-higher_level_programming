#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        big = None
    big = 0
    for i in my_list:
        if i > i + 1:
            big = i
        if big < i:
            big = i
    return big
