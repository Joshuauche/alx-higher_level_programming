#!/usr/bin/python3
"""
pascal Triangle
methods:
pascal_triangle
"""


def pascal_triangle(n):
    """
    list of lists of integers representing the Pascal’s triangle
    :param n:
    :return: the list of list for n
    """
    result = [[1]]

    # building the first row
    if n <= 0:
        return result
    for i in range(n - 1):
        # building a new temporary array not modifying the result list
        temp = [0] + result[-1] + [0]
        # building another empty row
        row = []
        # building the next row
        # it should be the length of previous row plus 1
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)
    return result
