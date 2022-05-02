#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = my_list[:]
    count = 0
    for i in my_list:
        if i % 2 == 0:
            res[count] = True
        else:
            res[count] = False
        count += 1
    return res
