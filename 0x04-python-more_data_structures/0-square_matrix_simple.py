#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newM = []
    for num in matrix:
        newM.append(list(map(lambda x: x ** 2, num)))
    return newM
