#!/usr/bin/python3
""" Rotates 2D matrix by 90 degrees """


def rotate_2d_matrix(matrix):
    """ Rotates 2D matrix by 90 degrees """
    if not isinstance(matrix, list):
        return
    if len(matrix) <= 0:
        return
    if not all(isinstance(x, list) for x in matrix):
        return
    rows = len(matrix)
    collumns = len(matrix[0])
    if not all(len(x) == collumns for x in matrix):
        return
    x, y = 0, rows - 1
    for i in range(collumns * rows):
        if i % rows == 0:
            matrix.append([])
        if y == -1:
            y = rows - 1
            x += 1
        matrix[-1].append(matrix[y][x])
        if x == collumns - 1 and y >= -1:
            matrix.pop(y)
        y -= 1
