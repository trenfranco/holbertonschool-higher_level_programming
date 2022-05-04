#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    for i, item in enumerate(new):
        if item == search:
            new[i] = replace
    return new
