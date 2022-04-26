#!/usr/bin/python3
n1 = 0
n2 = 0

for n1 in range(0, 10):
    for n2 in range(n1, 10):
        if n1 != n2 and n1 < n2:
            if (n1 != 8):
                print(f"{n1:d}", end="")
                print(f"{n2:d}", end=", ")
print("89")
