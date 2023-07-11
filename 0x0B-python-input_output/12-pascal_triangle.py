#!/usr/bin/python3
"""pascal triangle module"""


def pascal_triangle(n):
    """pascal_triangle
    arg:
        n: int
    return list of int list of pascal triangle
    """
    my_list = []
    if n <= 0:
        return my_list
    for row_num in range(n):
        my_row = [0] * (row_num + 1)
        if row_num == 0:
            my_row[0] = 1
            my_list.append(my_row)
            continue
        for i in range(row_num + 1):
            up = my_list[row_num - 1][i] if i <= row_num - 1 else 0
            up_left = my_list[row_num - 1][i - 1] if i - 1 >= 0 else 0
            my_row[i] = up + up_left
        my_list.append(my_row)
    return my_list
