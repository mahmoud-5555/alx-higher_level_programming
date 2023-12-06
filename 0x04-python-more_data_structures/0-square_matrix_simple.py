#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    if matrix is None:
        return res
    for i in range(len(matrix)):
        res.append(matrix[i].copy())
        for j in range(len(res[i])):
            res[i][j] = (res[i][j]) ** 2
    return res
