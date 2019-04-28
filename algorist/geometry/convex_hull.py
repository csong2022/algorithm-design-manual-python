#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Compute convex hulls of points in the plane using the Gries/Graham scan algorithm.

Translate from convex-hull.c.
"""

__author__ = "csong2022"

import types
from functools import cmp_to_key

from algorist.geometry.geometry import collinear, distance, ccw, Polygon, cw, Point


# Compute convex hulls of points in the plane using the
# Gries/Graham scan algorithm.

def convex_hull(_in: list, n: int) -> Polygon:
    if n <= 3:  # all points on hull!
        return Polygon(_in, n)

    _in = _in[0:n]
    _in.append(None)

    n = sort_and_remove_duplicates(_in, n)

    first_point = _in[0]  # first hull point

    _in[1: n] = sorted(_in[1: n], key=cmp_to_key(smaller_angle(first_point)))

    points = [Point(0, 0)] * (n + 1)  # convex hull points
    points[0] = first_point
    points[1] = _in[1]

    _in[n] = first_point  # sentinel to avoid special case

    top = 1  # current hull size
    i = 2

    while i <= n:
        if cw(points[top - 1], points[top], _in[i]):
            top -= 1  # top not on hull
        else:
            if not collinear(points[top - 1], points[top], _in[i]):
                top += 1
            points[top] = _in[i]
            i += 1

    return Polygon(points, top)


def sort_and_remove_duplicates(points: list, n: int) -> int:
    points[0: n] = sorted(points[0: n], key=cmp_to_key(leftlower))
    oldn = n  # number of points before deletion
    hole = 1  # index marked for potential deletion

    for i in range(1, oldn):
        if points[hole - 1] == points[i]:
            n -= 1
        else:
            points[hole] = points[i]
            hole += 1

    points[hole] = points[oldn - 1]
    return n


def leftlower(p1: Point, p2: Point) -> int:
    if p1.x < p2.x:
        return -1
    if p1.x > p2.x:
        return 1

    if p1.y < p2.y:
        return -1
    if p1.y > p2.y:
        return 1

    return 0


def smaller_angle(first_point: Point) -> types.FunctionType:
    def _smaller_angle(p1: Point, p2: Point) -> int:
        if collinear(first_point, p1, p2):
            if distance(first_point, p1) <= distance(first_point, p2):
                return -1
            else:
                return 1

        if ccw(first_point, p1, p2):
            return -1
        else:
            return 1

    return _smaller_angle
