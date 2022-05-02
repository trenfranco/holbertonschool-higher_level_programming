#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        big = None
    else:
        big = my_list[0]
        for i in my_list:
            if i > big:
                big = i
    return big
