#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Compute Euclidian distances.

Translate from distance.c.
"""

__author__ = "csong2022"


from math import sqrt


def distance(a: list, b: list) -> float:
    """
    Compute Euclidian distances

    :param a: vector a.
    :param b: vector b.
    :return: Euclidian distance between two vectors.
    """
    assert len(a) == len(b), 'Dimension mismatches'

    d = 0.0
    for i in range(len(a)):
        d += (a[i] - b[i]) * (a[i] - b[i])

    return sqrt(d)
