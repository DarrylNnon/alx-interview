#!/usr/bin/python3
"""A module that returns a pascal triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    triangle = []

    if n <= 0:
        return triangle
    for i in range(n):
        tmp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                tmp_list.append(1)
            else:
                tmp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(tmp_list)
    return triangle
