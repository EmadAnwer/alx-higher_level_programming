#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_divisible = []
    for num in my_list:
        is_divisible.append(num % 2 == 0)
    return is_divisible
