#!/usr/bin/python3
def no_c(my_string):
    news = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            news += i
    return news
