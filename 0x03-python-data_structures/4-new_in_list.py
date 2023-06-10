#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not (idx < 0 or idx > len(my_list) - 1):
        newl = my_list[:]
        newl[idx] = element
        return newl
    return my_list
