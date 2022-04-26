#!/usr/bin/python3
def uppercase(str):
    num = 0
    for element in str:
        num = ord(element)
        if (num > 96 and num < 123):
            num = num - 32
        print(f"{num:c}", end="")
    print()
