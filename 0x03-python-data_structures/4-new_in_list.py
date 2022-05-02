#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    size = len(my_list) - 1
    if idx < 0 or idx > size:
        return my_list
    a = my_list[:]
    a[idx] = element
    return a
