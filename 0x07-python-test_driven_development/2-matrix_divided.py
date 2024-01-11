#!/usr/bin/python3

"""	2_matrix_divaied
    this module has def matrix_divided(matrix, div):
    that dvaied all elemenrt by div
"""


def matrix_divided(matrix, div):
    result = []
    Erorr = "matrix must be a matrix (list of lists) of integers/floats"
    ''' the result list
    check if the matrix is empty
    '''
    if len(matrix) == 0:
        raise TypeError(Erorr)
    '''check div : is a number and not = 0'''

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    """
        save the length of the first row to check if the
        rows have the same number of the element
    """
    length_first_row = len(matrix[0])

    for row in matrix:
        """
            check each row : its length must be equal to
            the length of the first row
        """
        if len(row) != length_first_row:
            raise TypeError("Each row of the matrix must have the same size")
        """ uppend new row in result"""
        result.append([])

        for element in row:
            """check if the elements are numbers or not"""
            if not isinstance(element, (int, float)):
                raise TypeError(Erorr)

            """add new element to result"""
            result[-1].append(round((element / div), 2))

    return result
