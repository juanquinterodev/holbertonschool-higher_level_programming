#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    calc = []
    for i in matrix:
        row = list(map(lambda num: num ** 2, i))
        calc.append(row)
    return calc
