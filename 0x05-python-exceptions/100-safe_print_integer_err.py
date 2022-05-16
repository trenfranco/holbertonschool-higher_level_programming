#!/usr/bin/python3


import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        print()
        return True
    except (TypeError, ValueError) as e:
        print(e, file=sys.stderr)
        return False
