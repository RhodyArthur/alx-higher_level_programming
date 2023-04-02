#!/usr/bin/python3
"""
Matrix division Function
"""
def matrix_divided(matrix, div):
    """All elements of the matrix are divided by div, rounded to 2 decimal places"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(j / div, 2) for j in i] for i in matrix]
