#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxi = max(a_dictionary, key=lambda x: a_dictionary[x])
    return maxi
