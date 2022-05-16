#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    elements = 0

    try:
        for j in range(0, x):
            print(my_list[j], end="")
            elements += 1
        print()
        return elements
    except IndexError:
        print()
        return elements
