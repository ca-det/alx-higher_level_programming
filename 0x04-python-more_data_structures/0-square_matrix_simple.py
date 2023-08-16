#!/usr/bin/python3


def square_matrix_simple(matrix[]):
    new_list = []

    for x in matrix:
        new_list.append(list(map(lambda y: y**2, x)))
    return new_list
