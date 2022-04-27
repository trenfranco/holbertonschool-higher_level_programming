#!/usr/bin/python3
def fizzbuzz():
    fz = "FizzBuzz"
    f = "Fizz"
    b = "Buzz"
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print(f"{fz:s}", end=" ")
            continue
        elif i % 3 == 0:
            print(f"{f:s}", end=" ")
            continue
        elif i % 5 == 0:
            print(f"{b:s}", end=" ")
            continue
        else:
            print(f"{i:d}", end=" ")
