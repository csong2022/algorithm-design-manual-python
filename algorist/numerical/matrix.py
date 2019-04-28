# -*- coding: utf-8 -*-
"""
Multiply two matrices.

Translate from matrix.c.
"""


class Matrix:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.m = [[0] * (columns + 1) for i in range(rows + 1)]

    def print(self) -> None:
        for i in range(1, self.rows + 1):
            for j in range(1, self.columns + 1):
                print(" %d" % self.m[i][j], end='')
            print()
        print()


def read_matrix(_input) -> Matrix:
    rows, columns = list(map(int, _input.readline().split()))

    matrix = Matrix(rows, columns)

    for i in range(1, rows + 1):
        row = list(map(int, _input.readline().split()))
        matrix.m[i][1:] = row

    return matrix


def multiply(a: Matrix, b: Matrix) -> Matrix:
    if a.columns != b.rows:
        print("Error: bounds dont match!")
        return None

    c = Matrix(a.rows, b.columns)

    for i in range(1, a.rows + 1):
        for j in range(1, b.columns + 1):
            c.m[i][j] = 0
            for k in range(1, b.rows + 1):
                c.m[i][j] += a.m[i][k] * b.m[k][j]

    return c
