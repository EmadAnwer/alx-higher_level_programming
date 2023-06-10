#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for n in l:
            print("{:d}".format(n), end=' ' if n != l[-1] else '')
        print()
