#!/usr/bin/python3
def print_last_digit(number):
    last_diget = number - (10 * int(number / 10))
    if(last_diget < 0):
        last_diget *= -1
    print("{:d}".format(last_diget), end="")
    return last_diget
