#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, mul, div, add
    a = 10
    b = 5

    print(f"{a:d} + {b:d} = {add(a, b)}")
    print(f"{a:d} - {b:d} = {sub(a, b)}")
    print(f"{a:d} * {b:d} = {mul(a, b)}")
    print(f"{a:d} / {b:d} = {div(a, b)}")
