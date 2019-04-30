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

    def distance_to(self, b) -> float:
        d = (self.x - b.x) * (self.x - b.x) + (self.y - b.y) * (self.y - b.y)
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

    def parallel_q(self, l2) -> bool:
        """Are two lines parallel?"""
        return abs(self.a - l2.a) <= EPSILON and abs(self.b - l2.b) <= EPSILON

    def __eq__(self, l2):
        """Overrides the default implementation"""
        if isinstance(l2, Line):
            return self.parallel_q(l2) and abs(self.c - l2.c) <= EPSILON
        return False

    def intersection_point(self, l2) -> Point:
        """Intersection point of two lines."""
        if self == l2:
            print("Warning: Identical lines, all points intersect.")
            return Point(0.0, 0.0)

        if self.parallel_q(l2):
            print("Error: Distinct parallel lines do not intersect.")
            return None

        x = (l2.b * self.c - self.b * l2.c) / (l2.a * self.b - self.a * l2.b)

        if abs(self.b) > EPSILON:  # test for vertical line
            y = - (self.a * x + self.c) / self.b
        else:
            y = - (l2.a * x + l2.c) / l2.b

        return Point(x, y)

    def closest_point(self, p_in: Point) -> Point:
        """Closest point on the line."""
        if abs(self.b) <= EPSILON:  # vertical line
            x = -self.c
            y = p_in.y

            return Point(x, y)

        if abs(self.a) <= EPSILON:  # horizontal line
            x = p_in.x
            y = -self.c
            return Point(x, y)

        perp = Line.point_and_slope_to_line(p_in, 1 / self.a)  # non-degenerate line
        return self.intersection_point(perp)

    def print(self) -> None:
        print(str(self))

    def __str__(self):
        return "(a=%7.3lf,b=%7.3lf,c=%7.3lf)" % (self.a, self.b, self.c)


class Segment:
    """Line segment."""

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1  # endpoints of line segment
        self.p2 = p2

    def intersect(self, s2) -> bool:
        l1 = Line.points_to_line(self.p1, self.p2)
        l2 = Line.points_to_line(s2.p1, s2.p2)

        if l1 == l2:  # overlapping or disjoint segments
            return self.p1.point_in_box(s2.p1, s2.p2) or \
                   self.p2.point_in_box(s2.p1, s2.p2) or \
                   s2.p1.point_in_box(self.p1, self.p2) or \
                   s2.p2.point_in_box(self.p1, self.p2)

        if l1.parallel_q(l2):
            return False

        p = l1.intersection_point(l2)

        return p.point_in_box(self.p1, self.p2) and p.point_in_box(s2.p1, s2.p2)

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
        return not cw(self.a, self.b, p) and \
               not cw(self.b, self.c, p) and \
               not cw(self.c, self.a, p)

    def signed_area(self):
        return signed_triangle_area(self.a, self.b, self.c)

    def area(self):
        return abs(self.signed_area())

    def ccw(self):
        return self.signed_area() > EPSILON

    def cw(self):
        return self.signed_area() < -EPSILON

    def collinear(self):
        return self.area() <= EPSILON


def signed_triangle_area(a: Point, b: Point, c: Point) -> float:
    return (a.x * b.y - a.y * b.x + a.y * c.x - a.x * c.y + b.x * c.y - c.x * b.y) / 2.0


def triangle_area(a: Point, b: Point, c: Point) -> float:
    return abs(signed_triangle_area(a, b, c))


def ccw(a: Point, b: Point, c: Point) -> bool:
    return signed_triangle_area(a, b, c) > EPSILON


def cw(a: Point, b: Point, c: Point) -> bool:
    return signed_triangle_area(a, b, c) < -EPSILON


def collinear(a: Point, b: Point, c: Point) -> bool:
    return abs(signed_triangle_area(a, b, c)) <= EPSILON


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
