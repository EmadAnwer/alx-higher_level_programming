#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for i in range(len(l)):
            print("{:d}"
                  .format(l[i]), end=" " if (i != len(l) - 1) else "")
        print()
