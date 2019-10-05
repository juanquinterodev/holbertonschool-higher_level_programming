#!/usr/bin/python3
""" matrix-divided - Function that divide all elements of a matrix """


def matrix_divided(matrix, div):
    """
    check the matrix for it is a int or float
    check the div for every type
    check for the number if is 0 raise error message
    check for the length of the matrix
    return a matrix result
    """
    res_mat = []
    aux_mat = []
    errsize = "Each row of the matrix must have the same size"
    errmatrix = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or not len(matrix):
        raise TypeError(errmatrix)
    lenght = len(matrix[0])
    for i in matrix:
        if type(i) != list or not len(matrix):
            raise TypeError(errmatrix)
        if lenght != len(i):
            raise TypeError(errsize)
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError(errmatrix)
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    for i in matrix:
        aux_mat = list(map(lambda j: round((j / div), 2), [j for j in i]))
        res_mat.append(aux_mat)
    return res_mat
