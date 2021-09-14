#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in matrix[i]:
            if j != matrix[i] - 1:
                end = ' '
            else:
                end = ""
            print("{}".format(matrix[i][j]), end=end)
        print()
