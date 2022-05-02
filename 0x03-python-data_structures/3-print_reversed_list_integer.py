#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = my_list
    list.reverse(a)
    for i in a:
        print(f"{i:d}")
