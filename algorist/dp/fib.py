# -*- coding: utf-8 -*-
"""
Fibonacci Numbers.

Translate from fib.c.
"""
MAXN = 45  # largest n or m
UNKNOWN = -1  # contents denote an empty cell


def fib_r(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_r(n - 1) + fib_r(n - 2)


def fib_c(n: int, f: list) -> int:
    if f[n] == UNKNOWN:
        f[n] = fib_c(n - 1, f) + fib_c(n - 2, f)

    return f[n]


def fib_c_driver(n: int) -> int:
    f = [UNKNOWN] * (MAXN + 1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = UNKNOWN

    return fib_c(n, f)


def fib_dp(n: int) -> int:
    f = [UNKNOWN] * (MAXN + 1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


def fib_dp2(n: int) -> int:
    back1 = 1  # last two values of f[n]
    back2 = 0

    if n == 0:
        return 0

    for i in range(2, n):
        next = back1 + back2
        back2 = back1
        back1 = next

    return back1 + back2
