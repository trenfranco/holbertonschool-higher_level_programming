#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        number = number % 10
        print(f"{number:d}", end="")
        return number
    else:
        a = abs(number)
        a = a % 10
        print(f"{a:d}", end="")
        return a
