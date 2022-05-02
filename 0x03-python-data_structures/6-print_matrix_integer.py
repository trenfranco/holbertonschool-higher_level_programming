#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for cont in i:
            if i[-1] == cont:
                print(f"{cont:d}", end="")
            else:
                print(f"{cont:d}", end=" ")
        print()
