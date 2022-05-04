#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 == None or set_2 == None:
        return None
    hola=()
    hola = set_1.intersection(set_2)
    return hola

