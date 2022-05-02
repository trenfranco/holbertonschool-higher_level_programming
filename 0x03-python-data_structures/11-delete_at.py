#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > len(my_list) - 1 or idx < 0:
        return my_list
    my_list2 = my_list[:idx] + my_list[idx + 1:]
    my_list[:] = my_list2[:]
    return my_list
