#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    size = len(my_list) - 1
    if idx < 0 or idx > size:
        return my_list
    my_list[idx] = element
    return my_list
