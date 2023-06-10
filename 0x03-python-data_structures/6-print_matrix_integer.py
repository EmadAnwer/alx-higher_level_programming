#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        list_l = len(l)
        for i in range(list_l):
            print("{:d}".format(l[i]), end="")
            if (i != list_l - 1):
                print(" ", end="")
        print()
