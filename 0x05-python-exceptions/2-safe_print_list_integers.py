#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    elements = 0

    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            elements += 1
        except (IndexError):
            break
        except (TypeError, ValueError):
            pass
    print()
    return elements
