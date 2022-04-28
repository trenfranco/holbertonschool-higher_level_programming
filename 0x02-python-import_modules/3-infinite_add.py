#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    res = 0

    if count != 2:
        i = 1
        while i < count:
            res += int(sys.argv[i])
            i += 1
        print(f"{res:d}")

    else:
        print(f"{res:d}")
