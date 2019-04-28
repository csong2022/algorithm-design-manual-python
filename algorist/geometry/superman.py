# -*- coding: utf-8 -*-
"""
Compute Superman's flight path -- geometry example

Translate from superman.c.
"""
from math import sqrt, acos

from algorist.geometry.geometry import points_to_line, closest_point, distance, point_in_box, Point


def superman(s: Point, t: Point, c: list, ncircles: int) -> None:
    """
    Compute Superman's flight path -- geometry example

    :param s: Superman's initial position.
    :param t: target position.
    :param c: circles data structure
    :param ncircles: number of circles.
    :return: None
    """
    xray = 0.0  # length of intersection with circles
    around = 0.0  # length around circular arcs
    l = points_to_line(s, t)

    for i in range(1, ncircles + 1):
        close = closest_point(c[i].c, l)
        d = distance(c[i].c, close)

        if 0 <= d < c[i].r and point_in_box(close, s, t):
            xray += 2 * sqrt(c[i].r * c[i].r - d * d)
            angle = acos(d / c[i].r)
            around += 2 * angle * c[i].r
            print("circle %d (%7.3lf,%7.3lf,%7.3lf) is %7.3lf away from l, xray=%7.3lf around=%7.3lf angle=%7.3lf." %
                  (i, c[i].c.x, c[i].c.y, c[i].r, d, xray, around, angle))

    travel = distance(s, t) - xray + around
    print("Superman sees through %7.3lf units, and flies %7.3lf units" %
          (xray, travel))
