#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic geometric primitives and data types -- Lines, Circles, Segments

Translate from geometry.h, geometry.c.
"""

__author__ = "csong2022"

from math import sqrt

PI = 3.1415926  # ratio of circumference to diameter
EPSILON = 0.000001  # a quantity small enough to be zero
DIMENSION = 2  # dimension of points
MAXPOLY = 200  # maximum number of points in a polygon


class Point:
    """Point"""

    def __init__(self, x: float, y: float):
        self.x = x  # x-coordinat
        self.y = y  # y-coordinate

    @staticmethod
    def read_point(__input):
        line = __input.readline()
        if not line:
            return None
        else:
            x, y = list(map(float, line.split()))
            return Point(x, y)

    @staticmethod
    def read_points(_input) -> list:
        n = int(_input.readline()[:-1])  # number of points

        p = []
        for i in range(n):
            p.append(Point.read_point(_input))

        return p

    def distance_to(self, other) -> float:
        return Point.distance(self, other)

    @staticmethod
    def distance(a, b) -> float:
        d = (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)
        return sqrt(d)

    def point_in_box(self, b1, b2) -> bool:
        """Is point in box?"""
        return min(b1.x, b2.x) <= self.x <= max(b1.x, b2.x) and \
               min(b1.y, b2.y) <= self.y <= max(b1.y, b2.y)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return "(%lf,%lf)" % (self.x, self.y)

    def print(self) -> None:
        print("%7.3lf %7.3lf" % (self.x, self.y))

    @staticmethod
    def print_points(p: list, n: int) -> None:
        for i in range(n):
            print(str(p[i]))


class Line:
    """Line"""

    def __init__(self, a: float, b: float, c: float):
        self.a = a  # x-coefficient
        self.b = b  # y-coefficient
        self.c = c  # constant term

    @staticmethod
    def points_to_line(p1: Point, p2: Point):
        """Line pass the two points."""
        if p1.x == p2.x:
            a = 1
            b = 0
            c = -p1.x
        else:
            b = 1
            a = -(p1.y - p2.y) / (p1.x - p2.x)
            c = -(a * p1.x) - (b * p1.y)

        return Line(a, b, c)

    @staticmethod
    def point_and_slope_to_line(p: Point, m: float):
        """Line pass the point with given slope."""
        a = -m
        b = 1
        c = -(a * p.x + b * p.y)
        return Line(a, b, c)

    @staticmethod
    def parallel_q(l1, l2) -> bool:
        """Are two lines parallel?"""
        return abs(l1.a - l2.a) <= EPSILON and abs(l1.b - l2.b) <= EPSILON

    @staticmethod
    def same_line_q(l1, l2) -> bool:
        """Are they the same line?"""
        return Line.parallel_q(l1, l2) and abs(l1.c - l2.c) <= EPSILON

    @staticmethod
    def intersection_point(l1, l2) -> Point:
        """Intersection point of two lines."""
        if l1 == l2:
            print("Warning: Identical lines, all points intersect.")
            return Point(0.0, 0.0)

        if Line.parallel_q(l1, l2):
            print("Error: Distinct parallel lines do not intersect.")
            return None

        x = (l2.b * l1.c - l1.b * l2.c) / (l2.a * l1.b - l1.a * l2.b)

        if abs(l1.b) > EPSILON:  # test for vertical line
            y = - (l1.a * x + l1.c) / l1.b
        else:
            y = - (l2.a * x + l2.c) / l2.b

        return Point(x, y)

    @staticmethod
    def closest_point(p_in: Point, l) -> Point:
        """Closest point on the line."""
        if abs(l.b) <= EPSILON:  # vertical line
            x = -l.c
            y = p_in.y

            return Point(x, y)

        if abs(l.a) <= EPSILON:  # horizontal line
            x = p_in.x
            y = -l.c
            return Point(x, y)

        perp = Line.point_and_slope_to_line(p_in, 1 / l.a)  # non-degenerate line
        return Line.intersection_point(l, perp)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Line):
            return Line.same_line_q(self, other)
        return False

    def print(self) -> None:
        print(str(self))

    def __str__(self):
        return "(a=%7.3lf,b=%7.3lf,c=%7.3lf)" % (self.a, self.b, self.c)


class Segment:
    """Line segment."""

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1  # endpoints of line segment
        self.p2 = p2

    @staticmethod
    def segments_intersect(s1, s2) -> bool:
        l1 = Line.points_to_line(s1.p1, s1.p2)
        l2 = Line.points_to_line(s2.p1, s2.p2)

        if l1 == l2:  # overlapping or disjoint segments
            return s1.p1.point_in_box(s2.p1, s2.p2) or \
                   s1.p2.point_in_box(s2.p1, s2.p2) or \
                   s2.p1.point_in_box(s1.p1, s1.p2) or \
                   s2.p2.point_in_box(s1.p1, s1.p2)

        if Line.parallel_q(l1, l2):
            return False

        p = Line.intersection_point(l1, l2)

        return p.point_in_box(s1.p1, s1.p2) and p.point_in_box(s2.p1, s2.p2)

    def print(self) -> None:
        print("segment: ", end='')
        self.p1.print()
        self.p2.print()


class Polygon:
    """Polygon"""

    def __init__(self, p: list, n: int):
        self.p = p  # array of points in polygon
        self.n = n  # number of points in polygon

    def print(self) -> None:
        Point.print_points(self.p, self.n)


class Triangle:
    """Triangle"""

    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a  # point a
        self.b = b  # point b
        self.c = c  # point c

    def point_in_triangle(self, p: Point) -> bool:
        return not Triangle.cw(self.a, self.b, p) and \
               not Triangle.cw(self.b, self.c, p) and \
               not Triangle.cw(self.c, self.a, p)

    @staticmethod
    def signed_triangle_area(a: Point, b: Point, c: Point) -> float:
        return (a.x * b.y - a.y * b.x + a.y * c.x - a.x * c.y + b.x * c.y - c.x * b.y) / 2.0

    @staticmethod
    def triangle_area(a: Point, b: Point, c: Point) -> float:
        return abs(Triangle.signed_triangle_area(a, b, c))

    @staticmethod
    def ccw(a: Point, b: Point, c: Point) -> bool:
        return Triangle.signed_triangle_area(a, b, c) > EPSILON

    @staticmethod
    def cw(a: Point, b: Point, c: Point) -> bool:
        return Triangle.signed_triangle_area(a, b, c) < -EPSILON

    @staticmethod
    def collinear(a: Point, b: Point, c: Point) -> bool:
        return abs(Triangle.signed_triangle_area(a, b, c)) <= EPSILON


class Triangulation:
    def __init__(self, t: list, n: int):
        self.t = t  # indices of vertices in triangulation
        self.n = n  # number of triangles in triangulation

    def add_triangle(self, i: int, j: int, k: int) -> None:
        self.t.append([i, j, k])
        self.n += 1

    def print(self) -> None:
        for i in range(self.n):
            for j in range(3):
                print(" %d " % self.t[i][j], end='')
            print()


class Circle:
    """Circle."""

    def __init__(self, c: Point, r: float):
        self.c = c  # center of circle
        self.r = r  # radius of circle

    @staticmethod
    def read_circle(_input):
        line = _input.readline()
        x, y, r = list(map(float, line.split()))
        return Circle(Point(x, y), r)

    def print(self):
        print("%7.3lf %7.3lf %7.3lf" % (self.c.x, self.c.y, self.r))
