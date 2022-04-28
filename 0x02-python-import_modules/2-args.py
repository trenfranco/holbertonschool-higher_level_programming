#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argsnum = len(sys.argv)
    if argsnum == 2:
        print(f"{argsnum - 1:d} argument:")
        print(f"1: {sys.argv[1]}")
    elif argsnum > 2:
        print(f"{argsnum - 1:d} arguments:")
        i = 1
        while i < argsnum:
            print(f"{i:d}: {sys.argv[i]}")
            i += 1
    else:
        print("0 arguments.")
