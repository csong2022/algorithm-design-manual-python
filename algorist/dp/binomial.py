# -*- coding: utf-8 -*-
"""
Compute the binomial coefficients using dynamic programming.

Translate from binomial.c.
"""


def binomial_coefficient(n: int, m: int) -> int:
    """
    Compute the binomial coefficients using dynamic programming.

    :param n:
    :param m:
    :return:
    """
    assert m <= n

    bc = [[0] * (n + 1) for i in range(n + 1)]

    for i in range(n + 1):
        bc[i][0] = 1

    for j in range(n + 1):
        bc[j][j] = 1

    for i in range(n + 1):
        for j in range(1, i):
            bc[i][j] = bc[i - 1][j - 1] + bc[i - 1][j]

    return bc[n][m]
