#!/usr/bin/python3
def best_score(a_dictionary):
    max = -500
    if a_dictionary is None:
        return None
    for i in list(a_dictionary):
        if (a_dictionary[i] > max):
            max = a_dictionary[i]
            maxname = i
    return maxname
