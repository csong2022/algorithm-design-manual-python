# -*- coding: utf-8 -*-
"""
Triangulate a polygon via ear-clipping, and compute the area
of a polygon.

Translate from triangulate.c.
"""

from algorist.geometry.geometry import Polygon, Triangulation, Triangle, cw, Point, triangle_area


def triangulate(p: Polygon) -> Triangulation:
    left = [(i - 1 + p.n) % p.n for i in range(p.n)]  # left/right neighbor indices
    r = [(i + 1 + p.n) % p.n for i in range(p.n)]

    t = Triangulation([], 0)
    i = p.n - 2

    while t.n < p.n - 2:
        i = r[i]
        if ear_q(left[i], i, r[i], p):
            t.add_triangle(left[i], i, r[i])
            left[r[i]] = left[i]
            r[left[i]] = r[i]

    return t


def ear_q(i: int, j: int, k: int, p: Polygon) -> bool:
    t = Triangle(p.p[i], p.p[j], p.p[k])

    if cw(t.a, t.b, t.c):
        return False

    for m in range(p.n):
        if m != i and m != j and m != k:
            if point_in_triangle(p.p[m], t):
                return False

    return True


def point_in_triangle(p: Point, t: Triangle) -> bool:
    return not cw(t.a, t.b, p) and not cw(t.b, t.c, p) and not cw(t.c, t.a, p)


def area_triangulation(p: Polygon) -> float:
    t = triangulate(p)  # output triangulation

    total = 0.0
    for i in range(t.n):
        total += triangle_area(p.p[t.t[i][0]], p.p[t.t[i][1]], p.p[t.t[i][2]])

    return total


def area(p: Polygon) -> float:
    total = 0.0

    for i in range(p.n):
        j = (i + 1) % p.n
        total += (p.p[i].x * p.p[j].y) - (p.p[j].x * p.p[i].y)

    return total / 2.0
