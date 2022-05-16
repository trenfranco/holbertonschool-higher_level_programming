#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        res = a/b
    except ZeroDivisionError:
        res = None
    finally:
        if res is None:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(res))
    return res
