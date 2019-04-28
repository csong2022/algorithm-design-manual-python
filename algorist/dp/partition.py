#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Optimally balance partitions using dynamic programming.

Translate from partition.c.
"""

__author__ = "csong2022"

MAXINT = 100000  # infinity


def read_partition(_input):
    n, k = list(map(int, _input.readline().split()))
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = int(_input.readline()[:-1])

    return s, n, k


def print_books(s: list, start: int, end: int) -> None:
    print("{", end='')
    for i in range(start, end + 1):
        print(" %d " % s[i], end='')
    print('}')


def print_matrix(m: list, n: int, k: int) -> None:
    print()
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            print(" %d " % m[i][j], end='')
        print()


def reconstruct_partition(s: list, d: list, n: int, k: int) -> None:
    if k == 1:
        print_books(s, 1, n)
    else:
        reconstruct_partition(s, d, d[n][k], k - 1)
        print_books(s, d[n][k] + 1, n)


def partition(s: list, n: int, k: int) -> None:
    p = [0] * (n + 1)  # prefix sums array
    m = [[0] * (k + 1) for i in range(n + 1)]  # DP table for values
    d = [[0] * (k + 1) for i in range(n + 1)]  # DP table for dividers

    p[0] = 0  # construct prefix sums
    for i in range(1, n + 1):
        p[i] = p[i - 1] + s[i]
    for i in range(1, n + 1):
        m[i][1] = p[i]  # initialize boundaries
    for j in range(1, k + 1):
        m[1][j] = s[1]

    for i in range(2, n + 1):  # evaluate main recurrence
        for j in range(2, k + 1):
            m[i][j] = MAXINT
            for x in range(1, i):
                cost = max(m[x][j - 1], p[i] - p[x])
                if m[i][j] > cost:
                    m[i][j] = cost
                    d[i][j] = x

    reconstruct_partition(s, d, n, k)  # print book partition
