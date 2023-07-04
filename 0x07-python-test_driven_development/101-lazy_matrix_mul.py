#!/usr/bin/python3
"""Matrix multiplication using the module NumPy"""

from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul multiplies 2 matrices:
        m_a * m_b
    Arges:
        m_a: list of list
        m_b: list of list
    """
    # m_a or m_b is not a list
    return matmul(m_a, m_b)
