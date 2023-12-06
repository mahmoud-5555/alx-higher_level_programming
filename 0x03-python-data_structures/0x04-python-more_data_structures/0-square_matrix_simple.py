#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    if matrix is None:
        return res
    for i, it in enumerate(matrix):
        res.append(it)
        for j in range(len(res[i])):
            res[i][j] = (res[i][j]) ** 2
    return res
