#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    power_list = [[x ** 2 for x in rows] for rows in matrix]
    return power_list
