#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list) - 1
    if idx > size or idx < 0:
        return
    return my_list[idx]
