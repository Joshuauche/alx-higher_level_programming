#!/usr/bin/python3
"""
Defines a function that divides a matrix with an integer
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    if not (type(div) != int or type(div) != float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(type(num) == int or type(num) == float for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    quotient = [eval("{:.2f}".format(number / div)) for row in matrix for number in row]
    return quotient
