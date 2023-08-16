#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    simple_matrix = matrix.copy()
    for a in range(len(matrix)):
        simple_matrix[a] = list(map(lambda x: x**2, matrix[a]))
    return (simple_matrix)
