#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Compute the greatest common divisor of two integers.

Translate from gcd.c.
"""

__author__ = "csong2022"

from math import floor


def gcd1(p: int, q: int) -> int:
    """
    Compute the greatest common divisor of two integers

    :param p:
    :param q:
    :return:
    """
    if q > p:
        return gcd1(q, p)

    if q == 0:
        return p

    print(" gcd(%d,%d) &=& gcd(%d \\mod %d, %d) = gcd(%d,%d) " % (p, q, p, q, q, q, p % q))
    return gcd1(q, p % q)


def gcd(p: int, q: int) -> tuple:
    if q > p:
        g, x, y = gcd(q, p)
        return g, y, x

    if q == 0:
        return p, 1, 0

    g, x1, y1 = gcd(q, p % q)

    x = y1
    y = x1 - floor(p / q) * y1

    return g, x, y
