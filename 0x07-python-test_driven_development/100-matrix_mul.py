#!/usr/bin/python3
"""Matrix multiplication module"""


def matrix_mul(m_a, m_b):
    """matrix_mul multiplies 2 matrices:
        m_a * m_b
    Arges:
        m_a: list of list
        m_b: list of list
    """
    # m_a or m_b is not a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    # m_a or m_b is not list of lists
    if not all(isinstance(list_l, list) for list_l in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(list_l, list) for list_l in m_b):
        raise TypeError("m_b must be a list of lists")
    # m_a or m_b is empty
    if m_a in ([], [[]]):
        raise ValueError("m_a can't be empty")
    if m_b in ([], [[]]):
        raise ValueError("m_b can't be empty")
    # one element not int or flaot
    for row in m_a:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_b should contain only integers or floats")
    # ‘rows’ not same size
    row_len = len(m_a[0])
    for row in m_a:
        if len(row) != row_len:
            raise TypeError("each row of m_a must be of the same size")
    row_len = len(m_b[0])
    for row in m_b:
        if len(row) != row_len:
            raise TypeError("each row of m_b must be of the same size")
    # m_a and m_b can’t be multiplied
    len_of_columns_matrix_a = len(m_a[0])
    len_of_rows_matrix_b = len(m_b)
    if len_of_columns_matrix_a != len_of_rows_matrix_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for x in range(len(m_b)):
                result[i][j] += m_a[i][x] * m_b[x][j]
    return result
