#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(list(dict.fromkeys(my_list)))
